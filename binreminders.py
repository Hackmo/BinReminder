import json
from datetime import date
def sendmail():

    import smtplib, ssl
    from email.message import EmailMessage

    msg = EmailMessage()
    msg.set_content("One of your bins go out tomorrow!")

    msg['Subject'] = 'Bin Reminder!'
    msg['From'] = "SendersEmailAddress"
    msg['To'] = "RecipientsEmailAddress"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("LoginEmailHere", "YourEmailPasswordHere")
    server.send_message(msg)
    server.quit()

    return

with open('binschedule.json') as fd:
     json_data = json.load(fd)
     

a = json_data["date"]
today = str(date.today().strftime('%d/%m/%Y'))
if today in a:
    sendmail()

    
exit()
