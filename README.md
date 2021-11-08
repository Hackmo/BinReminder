# BinReminder
A simple python script that will read dates from a JSON file and emails you a reminder to put your bins out.


I got annoyed that I kept forgetting to check when my bins needed to go out so I built this script that will send me an email reminder the night before they are due to go out. No excuses to miss the collection now!


!!This is no longer relevant, i've removed smtplib and started using Yagmail. I'll update this soon.


The code is extremly simple and easy to follow but it works by using smtplib to send an email to a specified email address. The email is triggered by checking today's date against an array of dates in a JSON file. The dates in the JSON file are added manually. 

The name of my JSON file is "binschedule.json" but you can name it whatever you want. If you do change it just make sure to update this part of the code.

"with open('binschedule.json') as fd:" 

Replace 'binschedule.json' with your own JSON file. 

To get this to work for you, you will need to change some things.

 msg['From'] = "EnterSenderEmailhere"
 msg['To'] = "EnterRecipientEmailHere"

You will need to update the above with your own email in msg['From'] and enter the email address of who you want to receive the reminders. You can add a single email or multiple. To add multiple just separate the values with commas. For example.

msg['To'] = "example1@gmail.com", "example2@gmail.com" 

I made this with the purpose of using GMAIL to send the emails. To connect to gmails smptp server I use the following code.

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("login@example.com", "YourPasswordHere")

Replace "login@example.com" & "YourPasswordHere" with your own email & password.


if you want to change subject of the email, just edit

msg['Subject'] = 'Bin Reminder!'

Everything in between the '' will be set as the subject. 

To change the body of the email then edit

msg.set_content("One of your bins goes out tomorrow!")

Everything between the quotation marks will be set as the body of the email. 

That's it!
