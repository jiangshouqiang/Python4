import shutit

b = "echo Hello world"
session = shutit.create_session('bash')
session.send(b,echo=True)