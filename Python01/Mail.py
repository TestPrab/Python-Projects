import sys
import smtplib
import ssl
import getpass
sender=""
password=""
def Input():
     sender=input("Enter Sender's Mail Id ")
     password=getpass.getpass(prompt="Password :",stream=None)
def Login():
     try:
        server.login(sender,password)
        print("User Logged In successfully ")
        return 1
     except:
        print("Invalid Credentials ...press 1 to enter the email and password again else press 0 ")
        opt=input()
        if opt=="1":
            Input()
            Login()
        else:
           return 0

context=ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com",587) as server:
    try:
        server.connect("smtp.gmail.com",587)
        server.ehlo()
        server.starttls(context=context)
        print("Connection Established Successfully")
    except Exception as error:
        print("You are facing the following error: ")
        print(error)
        sys.exit(1)
    Input()
    Reciever=input("Enter the Reciever's Mail Address ")
    Message=input("Enter Your Message \n")
    result=Login()
    if(result==1):
        server.sendmail(sender,Reciever,Message)
        print("Mail Sent Successfully ")
        sys.exit(1)
    else:
        print(" Mail Not sent ")
        sys.exit(1)


 
