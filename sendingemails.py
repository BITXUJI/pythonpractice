from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


template = Template(Path("template.html").read_text())
# template.substitute()
message = MIMEMultipart()
message["from"] = "xuji"
message["to"] = "bitxuji@icloud.com"
message["subject"] = "this is a test"
body = template.substitute({"name": "John"})  # name =John is ok too
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("mosh.png").read_bytes()))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("bitxuji@gmail.com", "xj19940802")
    smtp.send_message(message)
    print("Sent...")
