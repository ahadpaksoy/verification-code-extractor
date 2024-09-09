import imaplib
import email
import re

# if you are using gmail you need to get a app password because gmail very strict about less secure apps.
# if you type here your real password gmail send authorization error.

def get_verification_code(email_address, email_password):
    # Connect to the email server (adjust settings as needed)
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, email_password)
    mail.select("inbox")

    # Search for the latest email
    _, search_data = mail.search(None, "ALL")
    latest_email_id = search_data[0].split()[-1]

    # Fetch the email body
    _, email_data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)
    
    # Extract the verification code (adjust the regex as needed)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode()
            # if your digits are different than 6, change the following code
            match = re.search(r'\b(\d{6})\b', body)
            if match:
                verification_code = match.group(1)
                verification_code_int = int(verification_code)
                return verification_code_int
    return None


def main():
    mail = "" # your mail address
    password = "" # your password and don't forget to enable imap

    get_verification_code(mail, password)


if __name__ == '__main__':
    main()
