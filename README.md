# Email Verification Code Extractor

This Python script connects to a Gmail account via IMAP, retrieves the latest email from the inbox, and extracts a 6-digit (you can change it as you wish ofc) verification code from the email's body. This is useful for automating processes that require verification codes sent via email.

## Requirements

- Python 3.x
- `imaplib` (standard library)
- `email` (standard library)
- `re` (standard library)

**Note:** If using Gmail, you need to enable "Less secure app access" or use an app-specific password if two-factor authentication (2FA) is enabled.

## Setup

1. **Install Dependencies**

   This script uses only standard Python libraries, so no additional installation is needed.

2. **Configure the Script**

   - Set `mail` and `password` variables in the `main()` function with your email address and password respectively.

   ```python
   def main():
       mail = "your_email@gmail.com"
       password = "your_password"
       get_verification_code(mail, password)
   ```

## Usage

1. Save the script to a file, e.g., `extract_verification_code.py`.
2. Run the script using Python:

   ```bash
   pip install requirements.txt
   python extract_verification_code.py
   ```

## How It Works

1. Connects to the Gmail IMAP server.
2. Logs in using provided email credentials.
3. Selects the inbox folder.
4. Searches for the latest email.
5. Fetches the email body.
6. Extracts a 6-digit verification code using a regular expression.

## Security Notice

- **Do not hardcode your email and password in the script**. Consider using environment variables or secure credential storage.
- Use app-specific passwords or OAuth 2.0 for Gmail to enhance security.

## License

This script is provided as-is, without any warranties. Feel free to use and modify it as needed.


Make sure to replace `"your_email@gmail.com"` and `"your_password"` in the `main()` function with your actual email credentials or configure a more secure method to handle credentials.
