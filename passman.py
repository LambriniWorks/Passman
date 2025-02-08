import sys
import hashlib
import base64
import json
import getpass
import time
import threading
import subprocess
import os
from cryptography.fernet import Fernet

# Function to generate deterministic passwords
def generate_password(master_password, site_name):
    combined = (master_password + site_name).encode()
    hashed = hashlib.pbkdf2_hmac('sha256', combined, b'secure_salt', 200000)
    return base64.urlsafe_b64encode(hashed)[:16].decode()

# Function to copy to clipboard (Cross-platform)
def copy_to_clipboard(text):
    system = os.name

    try:
        if system == "posix":  # Linux/macOS
            if os.system("which pbcopy > /dev/null 2>&1") == 0:
                subprocess.run(["pbcopy"], input=text.encode(), check=True)
            elif os.system("which xclip > /dev/null 2>&1") == 0:
                subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode(), check=True)
            elif os.system("which xsel > /dev/null 2>&1") == 0:
                subprocess.run(["xsel", "--clipboard", "--input"], input=text.encode(), check=True)
            elif os.system("which wl-copy > /dev/null 2>&1") == 0:  # For Wayland users
                subprocess.run(["wl-copy"], input=text.encode(), check=True)
            else:
                print("⚠️ No clipboard utility found. Copy manually.")
                return
        elif system == "nt":  # Windows
            subprocess.run("clip", input=text.encode(), check=True)

        print("✅ Password copied to clipboard (Will clear in 60 seconds).")

        # Start a background thread to clear clipboard after 60 seconds
        def clear_clipboard():
            time.sleep(60)
            if system == "posix":
                if os.system("which pbcopy > /dev/null 2>&1") == 0:
                    subprocess.run(["pbcopy"], input=b"", check=True)
                elif os.system("which xclip > /dev/null 2>&1") == 0:
                    subprocess.run(["xclip", "-selection", "clipboard"], input=b"", check=True)
                elif os.system("which xsel > /dev/null 2>&1") == 0:
                    subprocess.run(["xsel", "--clipboard", "--input"], input=b"", check=True)
                elif os.system("which wl-copy > /dev/null 2>&1") == 0:
                    subprocess.run(["wl-copy"], input=b"", check=True)
            elif system == "nt":
                subprocess.run("clip", input=b"", check=True)

        threading.Thread(target=clear_clipboard, daemon=True).start()

    except Exception as e:
        print(f"❌ Clipboard error: {e}")

# Function to derive an encryption key from the master password
def derive_key(master_password):
    key = hashlib.pbkdf2_hmac('sha256', master_password.encode(), b'unique_salt', 100000)
    return base64.urlsafe_b64encode(key)[:44]  # Fernet requires exactly 44 characters in base64

# Function to export transformation rules securely
def export_rules(rules):
    master_password = getpass.getpass("🔑 Enter master password to encrypt rules: ")
    key = derive_key(master_password)
    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(json.dumps(rules).encode())

    with open("passman-rules.enc", "wb") as f:
        f.write(encrypted_data)

    print("✅ Transformation rules exported successfully to 'passman-rules.enc'.")

# Function to import transformation rules securely
def import_rules():
    master_password = getpass.getpass("🔑 Enter master password to decrypt rules: ")
    key = derive_key(master_password)
    cipher = Fernet(key)

    try:
        with open("passman-rules.enc", "rb") as f:
            encrypted_data = f.read()

        decrypted_rules = json.loads(cipher.decrypt(encrypted_data).decode())

        print("✅ Rules imported successfully!")
        return decrypted_rules
    except Exception:
        print("❌ Error: Incorrect password or corrupted file.")
        return None

# Main Menu
def main():
    rules = {}

    while True:
        print("\n🔒 Passman Secure Password Manager 🔒")
        print("1️⃣ Generate a password")
        print("2️⃣ Export transformation rules")
        print("3️⃣ Import transformation rules")
        print("4️⃣ Exit")
        choice = input("Select an option: ")

        if choice == "1":
            site_name = input("🔐 Enter site name: ")
            master_password = getpass.getpass("🔑 Enter master password: ")
            password = generate_password(master_password, site_name)
            print(f"✅ Password for {site_name} generated.")

            # Copy password to clipboard
            copy_to_clipboard(password)

        elif choice == "2":
            export_rules(rules)

        elif choice == "3":
            rules = import_rules()

        elif choice == "4":
            print("🚀 Exiting Passman. Stay secure!")
            sys.exit(0)

        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()

