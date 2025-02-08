# Passo - The Last Password Manager You'll Ever Need

## What is Passo?
Passo is a stateless, offline-first password manager that generates your passwords on demand using transformation rules. Unlike traditional password managers:

- No password vaults - Nothing to steal. Nothing to sync.
- No cloud storage - Completely offline and secure.
- Mathematically generated passwords - Always reproducible.
- Encryption-protected transformation rules - Export and import securely.
- Auto-copy to clipboard - Prevents keylogging risks.
- Clipboard auto-clears after 60 seconds - No lingering passwords.

If there's nothing to steal, there's nothing to hack. Passo eliminates stored password vaults entirely.

## How It Works
1. You enter your Master Password and the Website/App Name.
2. Passo mathematically generates a unique password.
3. The password is copied to your clipboard and auto-clears in 60 seconds.
4. No passwords are stored. No vaults, no databases, no risks.

## Installation
### Install Dependencies
Make sure you have Python 3 installed. Then, install the required package:
```bash
pip install cryptography
```

### Download Passo
Clone the repository or download the script manually:
```bash
git clone https://github.com/LambriniWorks/Passo.git
cd Passo
```

### Move to a Hidden Directory for Security
```bash
mkdir -p ~/.passo
mv passo.py ~/.passo/
```

### Set Up Your Master Password
On first run, set up your Master Password:
```bash
python3 ~/.passo/passo.py --set-master
```
Follow the prompts to create a secure master password.

### Run Passo from Anywhere
For easy access, create a terminal alias:
```bash
echo 'alias passo="python3 ~/.passo/passo.py"' >> ~/.bashrc
source ~/.bashrc
```
Now, you can run Passo with:
```bash
passo
```

## Usage Guide
### Generate a Password
1. Run Passo:
   ```bash
   passo
   ```
2. Choose Option 1 and enter:
   - Website/App Name (e.g., `github.com`)
   - Your Master Password
3. The password is generated and copied to your clipboard.
4. Paste it where needed (clipboard clears after 60 seconds).

### Export Transformation Rules (Encrypted)
If you want to back up your rules:
```bash
passo
# Select Option 2 - Export Transformation Rules
```
This will generate `passo-rules.enc` in the current directory.

### Import Transformation Rules
To restore your transformation rules:
```bash
passo
# Select Option 3 - Import Transformation Rules
```

## Why Passo is Different
Passo doesn't store passwords. Instead, it re-creates them on demand, making them unhackable.

Even if your device is stolen, there’s nothing to steal. Your passwords are never stored—just mathematically derived.

You control your transformation rules. Securely export/import them whenever needed.

Better than LastPass, Bitwarden, and 1Password. No vaults, no sync, no servers—just security.

## Spread the Word
If you think Passo is worth it, share it.
- Star the repo on GitHub
- Post it on Reddit, Hacker News, or anywhere people care about security
- Contribute if you want to improve it

GitHub Repo: [https://github.com/LambriniWorks/Passo](https://github.com/LambriniWorks/Passo)

Passo - The Last Password Manager You'll Ever Need.


