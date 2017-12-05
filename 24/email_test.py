import smtplib
from email.message import EmailMessage

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtp.ehlo()	# 테스트 hello

smtp.login('dchkang83@gmail.com', 'password111')
#...
#smtp.quit()	# 접속 끊기


msg = EmailMessage()
msg['Subject'] = '안녕하세요'
msg['From'] = ''
msg['to'] = 'dchkang83@naver.com'

msg.set_content('''
safsadf
safasd
sadf
df
''')

smtp.send_message(msg)
smtp.quit()