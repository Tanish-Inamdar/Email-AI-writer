// this is the actual bot
from write_emails import create_email
from send_emails import send_email

MessageF = create_email()
subject= input("Subject of the Email: ")
to = input("To whom shall this fine email send to: ")

send_email(to = to, subject= subject, message= MessageF) 
