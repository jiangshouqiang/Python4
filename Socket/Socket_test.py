import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# s.settimeout(10)
# print(s.accept())
buffer = []
while True:
    d = s.recv(1024)
    if d :
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
print(data)