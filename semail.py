import smtplib
import email.message

def enviar_email(email_body):
    import smtplib
    import email.message
    import dotenv
    import os 
    dotenv.load_dotenv(dotenv.find_dotenv())
    username= os.getenv('sm')

    
    
    dest_email=input('\033[33mEmail to:\033[m ')
    msg=email.message.Message()
    msg['Subject']= 'Password or username recovery'
    msg['From']= 'pythonban4545@gmail.com'
    msg['To']= dest_email
    password= username
    msg.add_header('Content-Type','text/html')
    msg.set_payload(email_body)
    s=smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #Login
    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
    print('\033[32mEmail sent!\033[m')



