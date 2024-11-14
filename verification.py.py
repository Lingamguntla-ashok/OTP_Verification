#imports some modules like random module,MIMEMultipart module and MIMEText
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Generated a four or six digit number which digit you want
otp = random.randint(1111,9999)

#write smtp_server and port number
smtp_server = "smtp.gmail.com"
smtp_port = 587

#write user mail id and user generated password with help of "https://myaccount.google.com/apppasswords"
mailusername = "lingamguntlaashok44@gmail.com"
mailpassword = "zumx rzob uxkr xfyw"

#write sender mail id
from_email = "lingamguntlaashok44@gmail.com"

#Enter the Resever mail id
to_email = input("Enter mail id: ")

#Enter the subject in the resever id
subject = "OTP For Verification"

#write body of the given mail
body = f"Otp for Verification is {otp}\n\nThanks for choosing codegnan"

#calleing the MIMEMultipart module
msg = MIMEMultipart()           
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain'))

#Calling the server
server = smtplib.SMTP(smtp_server,smtp_port)     
server.starttls()
server.login(mailusername,mailpassword)
server.send_message(msg)
 #Verify otp in then you write the condiction the otp validate or not
verifyotp = int(input(f"Enter OTP sent to your mail ({to_email}): ")) 
if verifyotp == otp:
    print("Verification sucessfull")
else:
    print("Verification Failed")