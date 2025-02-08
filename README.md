# Passman - The Last Password Manager You'll Ever Need

## What is Passman?
Passman is a stateless, offline-first password manager that generates your passwords on demand using transformation rules. Unlike traditional password managers:

- No password vaults - Nothing to steal. Nothing to sync.
- No cloud storage - Completely offline and secure.
- Mathematically generated passwords - Always reproducible.
- Encryption-protected transformation rules - Export and import securely.
- Auto-copy to clipboard - Prevents keylogging risks.
- Clipboard auto-clears after 60 seconds - No lingering passwords.

If there's nothing to steal, there's nothing to hack. Passman eliminates stored password vaults entirely.

## How It Works
1. You enter your Master Password and the Website/App Name.
2. Passman mathematically generates a unique password.
3. The password is copied to your clipboard and auto-clears in 60 seconds.
4. No passwords are stored. No vaults, no databases, no risks.

## Installation
### Install Dependencies
Make sure you have Python 3 installed. Then, install the required package:
```bash
pip install cryptography
```

### Download Passman
Clone the repository or download the script manually:
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Passman.git
cd Passman
```

### Move to a Hidden Directory for Security
```bash
mkdir -p ~/.passman
mv passman.py ~/.passman/
```

### Set Up Your Master Password
On first run, set up your Master Password:
```bash
python3 ~/.passman/passman.py --set-master
```
Follow the prompts to create a secure master password.

### Run Passman from Anywhere
For easy access, create a terminal alias:
```bash
echo 'alias passman="python3 ~/.passman/passman.py"' >> ~/.bashrc
source ~/.bashrc
```
Now, you can run Passman with:
```bash
passman
```

## Usage Guide
### Generate a Password
1. Run Passman:
   ```bash
   passman
   ```
2. Choose Option 1 and enter:
   - Website/App Name (e.g., `github.com`)
   - Your Master Password
3. The password is generated and copied to your clipboard.
4. Paste it where needed (clipboard clears after 60 seconds).

### Export Transformation Rules (Encrypted)
If you want to back up your rules:
```bash
passman
# Select Option 2 - Export Transformation Rules
```
This will generate `passman-rules.enc` in the current directory.

### Import Transformation Rules
To restore your transformation rules:
```bash
passman
# Select Option 3 - Import Transformation Rules
```

## Why Passman is Different
Passman doesn't store passwords. Instead, it re-creates them on demand, making them unhackable.

Even if your device is stolen, there’s nothing to steal. Your passwords are never stored—just mathematically derived.

You control your transformation rules. Securely export/import them whenever needed.

Better than LastPass, Bitwarden, and 1Password. No vaults, no sync, no servers—just security.

## Spread the Word
If you think Passman is worth it, share it.
- Star the repo on GitHub
- Post it on Reddit, Hacker News, or anywhere people care about security
- Contribute if you want to improve it

GitHub Repo: [https://github.com/YOUR_GITHUB_USERNAME/Passman](https://github.com/YOUR_GITHUB_USERNAME/Passman)

Passman - The Last Password Manager You'll Ever Need.


