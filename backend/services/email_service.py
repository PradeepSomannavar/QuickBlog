import smtplib
from email.message import EmailMessage
import os

def send_email(subject: str, body: str, to_emails: list[str]):
    """
    Send an email to a list of recipients using SMTP.
    SMTP server configuration is read from environment variables:
    SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD
    """
    smtp_server = os.getenv("SMTP_SERVER", "smtp.example.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME", "your_username")
    smtp_password = os.getenv("SMTP_PASSWORD", "your_password")
    from_email = smtp_username

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print(f"Email sent to {len(to_emails)} recipients.")
    except Exception as e:
        print(f"Failed to send email: {e}")
