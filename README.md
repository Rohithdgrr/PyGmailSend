# PyGmailSend
Simple Python Tool to Send Emails with Gmail SMTP


Email Sender
A simple command-line tool to send emails using Python's smtplib and Gmail's SMTP server. This tool allows users to send emails by providing their Gmail address, app password, recipient's email, subject, and body.

Project Structure

email_sender/
├── src/
│   └── email_sender.py   # Main script with email-sending functionality
├── docs/
│   └── usage.md          # Detailed usage instructions
├── requirements.txt       # Project dependencies
└── README.md             # Project overview

Prerequisites
Python 3.8+
A Gmail account with an App Password (required for Gmail's two-factor authentication)

Installation
Clone the repository:git clone https://github.com/yourusername/email_sender.git
cd email_sender


Install dependencies:pip install -r requirements.txt
Note: This project uses Python's standard library (smtplib and email), so no additional packages are required.

Usage
Run the script and follow the prompts:
python src/email_sender.py

Steps
Enter your Gmail address.
Enter your Gmail App Password (not your regular password; see Google's App Password guide).
Enter the recipient's email address.
Enter the email subject.
Enter the email body.

Dependencies
Python standard library: smtplib, email.message

Contributing
Fork the repository
Create a feature branch (git checkout -b feature/new-feature)
Commit changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature/new-feature)
Create a Pull Request

