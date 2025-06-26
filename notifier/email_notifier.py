import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


def send_email_alert(items):
    """
    Send an email alert with auction item results.
    
    Args:
        items (list): List of dictionaries with 'title' and 'link' keys
    """
    # Load environment variables
    load_dotenv()
    
    sender_email = os.getenv('EMAIL_SENDER')
    sender_password = os.getenv('EMAIL_PASSWORD')
    recipient_email = os.getenv('EMAIL_RECIPIENT')
    
    if not all([sender_email, sender_password, recipient_email]):
        raise ValueError("Missing email configuration in .env file")
    
    # Format the email content
    subject = f"Auction Alert: {len(items)} items found"
    
    # Create email body
    body = f"Found {len(items)} matching auction items:\n\n"
    
    for i, item in enumerate(items, 1):
        body += f"{i}. {item['title']}\n"
        body += f"   Link: {item['link']}\n\n"
    
    body += "\nHappy bidding! 🎯"
    
    # Create message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}") 