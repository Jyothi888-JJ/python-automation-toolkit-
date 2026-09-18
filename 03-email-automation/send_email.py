import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(subject, body, recipient_list, pdf_file):
    sender_email = "your_email@gmail.com"
    app_password = "your_app_password"  # Generated Google App Password

    for recipient in recipient_list:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        if pdf_file:
            with open(pdf_file, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype="pdf")
                attach.add_header('Content-Disposition', 'attachment', filename=pdf_file)
                msg.attach(attach)
                
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {recipient}")

recipients = ["user1@example.com", "user2@example.com"]
send_email("Masterclass Notification", "Join our free webinar!", recipients, "class_details.pdf")
