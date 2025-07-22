import smtplib
from email.message import EmailMessage

def send_email(sender_email: str, app_password: str, receiver_email: str, subject: str, body: str) -> None:
    """Send an email using Gmail's SMTP server.

    Args:
        sender_email: The sender's Gmail address.
        app_password: The app-specific password for Gmail.
        receiver_email: The recipient's email address.
        subject: The subject line of the email.
        body: The body content of the email.
    """
    # Create email message
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.set_content(body)

    # Connect to Gmail SMTP server and send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, app_password)  # Authenticate with app password
            server.send_message(email)
            print("Email sent successfully!")
    except Exception as error:
        print(f"Failed to send email: {error}")

def main() -> None:
    """Main function to collect user input and send an email."""
    sender_email = input("Enter your Gmail address: ")
    app_password = input("Enter your Gmail App Password: ")
    receiver_email = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    send_email(sender_email, app_password, receiver_email, subject, body)

if __name__ == "__main__":
    main()