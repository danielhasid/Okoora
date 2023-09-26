import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText


def send_email():

    sender = "qa@okoora.com"
    to = "danielh@okoora.com"

    # attachment = "C:/Users/DanielHasid/PycharmProjects/Automation/Tests/report.html"
    html = open("C:/Users/DanielHasid/PycharmProjects/Automation/Tests/report.html")
    msg = MIMEText(html.read(), 'html')
    msg['Subject'] = "Regression report"
    msg['Body'] = "find the attachment"
    msg['From'] =sender
    msg['To'] = to
    text = msg.as_string()
    # part = MIMEBase('application', "octet-stream")
    # part.set_payload(open(attachment, "rb").read())
    # encoders.encode_base64(part)
    #
    # # part.add_header('Content-Disposition', 'attachment', filename=attachment)
    #
    # msg.attach(part)

    with smtplib.SMTP('okoora-com.mail.protection.outlook.com',25) as server:
        # server.ehlo()
        server.starttls()
        # server.ehlo()
        server.sendmail(sender,to,text)
        server.quit()

send_email()