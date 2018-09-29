from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'pythonchaintest@126.com' #input("Form:")
password = 'j123123'#input("password:")
to_addr = '284923424@qq.com'#input("To :")
smtp_server = 'smtp.126.com'#input("SMTP server :")

msg = MIMEText('Hello , send by python ...','plain','utf-8 ')
msg['From'] = _format_addr('Python 爱好者<%s>' % to_addr)
msg['To']   = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()