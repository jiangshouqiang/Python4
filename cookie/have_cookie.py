
from http import cookiejar
from urllib import request
import os

ckjar = cookiejar.MozillaCookieJar(os.path.join('./'))
req = request.Request(url,postdata,header)

