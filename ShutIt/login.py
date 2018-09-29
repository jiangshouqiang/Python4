import shutit

session = shutit.create_session('bash')

session.login('ssh 192.168.11.191',user='veradm',password='hibaby@)!&')
session.send('hi',echo=True)
session.logout()