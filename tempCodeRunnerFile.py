import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=30)
server.ehlo()
