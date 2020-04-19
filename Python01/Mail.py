import sys
import smtplib
import ssl
import getpass
sender=" "
password=" "
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
    sender=input("Enter you email ID")
    password=getpass.getpass(prompt="Password")
    Reciever=input("Enter the Reciever's Mail Address ")
    Message=input("Enter Your Message \n")
    try:
        server.login(sender,password)
        print("User Logged In successfully ")
        server.sendmail(sender,Reciever,Message)
        print("Mail Sent Successfully ")
        sys.exit(1)
    except Exception as Error:
        print(Error,"\n")
        print("Invalid Credentials ...press 1 to enter the email and password again else press 0 ")
        opt=input()
        if opt=="1":
            sender=input("Enter you email ID")
            password=getpass.getpass(prompt="Password") 
            try:
             server.login(sender,password)
             print("User Logged In successfully ")
             server.sendmail(sender,Reciever,Message)
             print("Mail Sent Successfully ")
             sys.exit(1)
            except:
                print(" Was not able to login ...closing connection and exiting ")
                server.quit()
                sys.exit(1)
        else:
           print(" Mail Not sent ")
           sys.exit(1) 
    try:
     server.sendmail(sender,Reciever,Message)
     print("Mail Sent Successfully ")
     sys.exit(1)
    except:
        print(" Was not able to login ...closing connection and exiting ")
        server.quit()
        sys.exit(1)
       
