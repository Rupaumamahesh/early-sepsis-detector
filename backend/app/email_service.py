import smtplib
from email.mime.text import MIMEText

def send_email(summary):
    sender_email = "acksharavaradhu@gmail.com"
    sender_password = "zlaclpktqogfvkll"
    receiver_email = "avengers202603@gmail.com"

    msg = MIMEText(summary)
    msg["Subject"] = "Sepsis Alert Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        print("STEP A: Connecting to server")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        print("STEP B: Logging in")

        server.login(sender_email, sender_password)

        print("STEP C: Sending email")

        server.send_message(msg)

        print("✅ EMAIL SENT SUCCESSFULLY")

        server.quit()
        return True

    except Exception as e:
        import traceback
        print("❌ EMAIL ERROR:")
        traceback.print_exc()
        return False