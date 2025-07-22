Email Sender Usage Guide
Overview
This tool allows you to send emails via Gmail's SMTP server using Python's smtplib library. It prompts for the sender's Gmail address, app password, recipient's email, subject, and body, then sends the email.
Setup

Ensure you have Python 3.8+ installed.
Generate a Gmail App Password:
Go to Google Account Security.
Enable 2-Step Verification if not already enabled.
Under "2-Step Verification," select "App passwords."
Create a new app password for "Mail" and note it down (you won't see it again).



Running the Tool
Navigate to the project directory:cd email_sender
Run the script:python src/email_sender.py



User Input
Gmail Address: Your Gmail address (e.g., yourname@gmail.com).
App Password: The 16-character app password generated from Google.
Recipient's Email: The email address of the recipient.
Subject: The subject line of the email.
Body: The content of the email.

Troubleshooting
Authentication Error: Ensure you are using a valid Gmail App Password, not your regular Gmail password.
Connection Issues: Check your internet connection or verify Gmail's SMTP settings (smtp.gmail.com, port 587).
Invalid Email Address: Ensure the recipient's email address is valid.
