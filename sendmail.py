import smtplib 


gmail = ""
password = "";

to = input("To :")
sub = input("Subject :")
msg = input("Enter Your Message :")
def sendMail(to,sub,msg):
    print(f"email to {to} send with subject is:{sub} and Message {msg}")
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(gmail,password)

    s.sendmail(gmail,to,f"subject: {sub}\n\n{msg}")
    s.quit()


sendMail(to,sub,msg)
