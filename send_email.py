import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_gmail(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using Gmail's SMTP server.

    Args:
        sender_email (str): The sender's Gmail address.
        sender_password (str): The sender's Gmail account password or App Password.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        body (str): The body of the email.
    """
    try:
        # Connect to Gmail's SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # Port for TLS

        # Create a secure SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        
        # Log in to the Gmail account
        server.login(sender_email, sender_password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

    finally:
        server.quit()  # Always close the server connection


# send_email_gmail("risingabhi@gmail.com", "sjpqrxgjvlnrtseu", "tdi@thinkstudio.in", "test", "this is test mail")