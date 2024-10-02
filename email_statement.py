
import os
import smtplib
import dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#Mandar PDF
def email_pdf(user):
    dotenv.load_dotenv(dotenv.find_dotenv())
    password = os.getenv('sm')
    dest_email = input('\033[33mEmail to:\033[m ')

    msg = MIMEMultipart()
    msg['Subject'] = f'Your statement is ready, <{user}>!'
    msg['From'] = 'pythonban4545@gmail.com'
    msg['To'] = dest_email


    body = "Here is your statement."
    msg.attach(MIMEText(body, 'plain'))


    with open('statement.pdf', 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='statement.pdf')
        msg.attach(part)


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    print('\033[32mEmail sent!\033[m')


#Mandar HTML
def email_html(user, ini_bal, deposit, total_deposits, withdrawal, total_withdrawals, initial_balance):
    import smtplib
    import email.message
    import dotenv
    import os
    from datetime import datetime
    dotenv.load_dotenv(dotenv.find_dotenv())
    username = os.getenv('sm')

    dest_email = input('\033[33mEmail to:\033[m ')
    msg = email.message.Message()
    msg['Subject'] = 'Password or username recovery'
    msg['From'] = 'pythonban4545@gmail.com'
    msg['To'] = dest_email
    password = username

    agora = datetime.now()
    data_hora_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")

    msg.add_header('Content-Type', 'text/html')

    # Concatenate all parts into one HTML string
    html_content = f"""
    <html>
        <body>
            <p>{data_hora_formatada}</p>
            <h2 style="color: purple;">STATE BANK</h2>
            <p><span style="color: blue;">Here is your Statement</span>, {user}</p>
            <p><span style="color: blue;">Initial Balance</span>: <span style="color: black;">${ini_bal}</span></p>
            <p><span style="color: blue;">Deposits Made</span>: <span style="color: black;">{deposit}</span></p>
            <p><span style="color: blue;">Total Deposits</span>: <span style="color: black;">${total_deposits}</span></p>
            <p><span style="color: blue;">Withdrawals Made</span>: <span style="color: black;">{withdrawal}</span></p>
            <p><span style="color: blue;">Total Withdrawals</span>: <span style="color: black;">${total_withdrawals}</span></p>
            <p><span style="color: blue;">Ending Balance</span>: <span style="color: black;">${initial_balance}</span></p>
        </body>
    </html>
    """


    msg.set_payload(html_content)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('\033[32mEmail sent!\033[m')




