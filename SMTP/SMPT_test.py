from email.mime.text import MIMEText

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>',"html",'utf-8')

from_addr = input('From:')
password = input('Password:')

to_addr = input('To:')
smtp_server = input('SMTP sever:')

import smtplib

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#  test
# From:jiangshouqiang@symdata.cn
# Password:jsq1998
# To:284923424@qq.com
# SMTP sever:smtp.ym.163.com