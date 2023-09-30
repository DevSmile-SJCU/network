import smtplib
from email.mime.text import MIMEText

# 네이버 이메일 로그인 정보
user = 'xxxxx'
password = 'yyyyy'

# 이메일 구성
subject = "세종사이버대학교 환영 메시지"
content = "안녕하세요. 세종사이버대학교 입니다."
receiver = 'zzzzz'

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = user
msg['To'] = receiver

# 네이버 이메일 서버에 연결
with smtplib.SMTP_SSL('smtp.naver.com', 465) as server:
    server.login(user, password)  # 로그인
    server.sendmail(user, receiver, msg.as_string())  # 이메일 발송

print('이메일이 성공적으로 발송되었습니다.')
