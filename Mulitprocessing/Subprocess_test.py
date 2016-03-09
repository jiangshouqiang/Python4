import subprocess
print("$ nslookup www.python.org")
r = subprocess.call(['nsloopup','www.python.org'])
print("Exit code : " , r)