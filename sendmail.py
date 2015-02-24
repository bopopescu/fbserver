import smtplib
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login()
server.sendmail('chaluemwut@gmail.com','chaluemwut@hotmail.com','data sender')
server.quit()
