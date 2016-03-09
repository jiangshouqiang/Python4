from urllib import request
import json
from urllib import parse
import html
print(dir(html))
with request.urlopen("http://www.ifeng.com/") as fh:
    htmls = fh.read().decode("utf8")
    # print(html.escape(htmls))

