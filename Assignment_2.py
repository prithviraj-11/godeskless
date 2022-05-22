import smtplib
gmail_user="senders email address"
sender=""
receivers=""
subject=""
body=""

sent_from=gmail_user
sender_password=input("Enter sender's Email password: ")
receivers=input("Enter receivers Email address: ")
subject=input("Enter Subject of the Email: ")
body=input("Enter Body of the Email: ")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, "".join(receivers), subject, body)

try: 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.starttls() 
    smtp.login(gmail_user,sender_password) 
    smtp.sendmail(gmail_user, receivers,email_text)  
    smtp.quit() 
    print("Email sent successfully!") 

except Exception as ex: 
    print("Error: Something went wrong",ex)