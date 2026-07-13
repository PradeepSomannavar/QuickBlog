import smtplib
import os
from email.message import EmailMessage


def send_email(subject: str, body: str, to_emails: list[str]):
    smtp_server = os.getenv("SMTP_SERVER", "")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")

    if not smtp_server or not smtp_username:
        print("[email] SMTP not configured — skipping email notification.")
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_username
    msg["To"] = ", ".join(to_emails)
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print(f"[email] Sent to {len(to_emails)} recipients.")
    except Exception as e:
        print(f"[email] Failed to send: {e}")
