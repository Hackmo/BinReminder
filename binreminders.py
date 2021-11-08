import yagmail
import json
from datetime import date

def sendmail():
    
    receiver = "ReceiverEmailhere"
    body = ["One of your bins goes out tomorrow! " "\n" "\n
            "Check the attachment to find out which one!"]
    filename = "binschedule.pdf"

    yag = yagmail.SMTP('SenderEmailHere', 'YourPasswordHere')
    yag.send(
        to=receiver,
        subject="Bin Reminder!",
        contents=body, 
        attachments=filename,
    )
    return
    

with open('binschedule.json') as fd:
     json_data = json.load(fd)
     

a = json_data["date"]
today = str(date.today().strftime('%d/%m/%Y'))
if today in a:
    sendmail()

exit()
