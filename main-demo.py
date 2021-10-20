import smtplib 

sender_email = "emailsend@gmail.com"
rec_email = "emailrecive@gmail.com"
#Password Sender_Email
password = input(str("Enter your login password to confirm: "))
subject = "Title Email"
chat = "What you want to say\nLine2"
message = f"Subject: {subject}\n\n{chat}"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success !!")
server.sendmail(sender_email, rec_email, message)
print("Email was sent to ", rec_email)