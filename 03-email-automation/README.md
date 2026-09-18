# Automated Customized Email Campaign with PDF Attachments

This project demonstrates a simple **Python email automation script** that sends individually addressed emails to multiple recipients with an optional PDF attachment.

## What This Script Does

1. Takes a list of email recipients.
2. Creates an email for each recipient.
3. Adds a subject and message body.
4. Attaches a PDF file.
5. Connects to Gmail's SMTP server.
6. Sends the email automatically to each recipient.

## Technologies Used

* Python
* SMTP
* Gmail
* `smtplib`
* `email` module
* MIME attachments

## How It Works

```text
Recipient List
      ↓
Create Email
      ↓
Add Message + PDF
      ↓
Connect to Gmail SMTP
      ↓
Authenticate
      ↓
Send Email
      ↓
Next Recipient
```

## Setup

### 1. Prepare your Gmail account

Enable two-factor authentication and generate a **Google App Password** for SMTP authentication.

### 2. Install Python

No external Python libraries are required because the script uses Python's built-in `smtplib` and `email` modules.

### 3. Configure the Script

Update the following values:

```python
sender_email = "your_email@gmail.com"
app_password = "your_app_password"
```

Also update the recipient list and PDF filename:

```python
recipients = ["user1@example.com", "user2@example.com"]

send_email(
    "Masterclass Notification",
    "Join our free webinar!",
    recipients,
    "class_details.pdf"
)
```

### 4. Run the Script

```bash
python email_automation.py
```

## Example Output

```text
Email sent successfully to user1@example.com
Email sent successfully to user2@example.com
```

## Security Note

**Do not upload your Gmail App Password or other credentials to GitHub.**

For a real project, credentials should be stored using **environment variables or a secrets manager** instead of hard-coding them in the Python script.

## Purpose

This project demonstrates how **Python can automate repetitive email communication**, including personalized recipients and PDF attachments.
