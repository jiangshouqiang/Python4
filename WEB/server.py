from wsgiref.simple_server import  make_server
from Web_test import application


httpd = make_server('',8000,application)
print('Serving HTTP on port 8000 ...')
httpd.serve_forever()