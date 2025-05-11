import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, content):
    from_email = "Your-Email"  #Replace Your ID
    app_password = "Your-Password"  # 🔐 Replace with env variable in production

    message = MIMEMultipart("alternative")
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Add both plain and HTML parts
    message.attach(MIMEText(content, 'plain'))
    message.attach(MIMEText(f"<html><body><p>{content}</p></body></html>", 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.send_message(message)
        print("📧 Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
