import re

re_mobile = '.*\d{1,}.*'
print(re.match(re_mobile,'klj;4dakf'))

re_url = r'^https://www.tianyancha.com/.*'
urls = 'https://www.tianyancha.com/search/ola3?key=233&searchType=company'
print(re.match(re_url,urls))

bool1 = re.match(r'^\d{3}\-\d{3,8}$','010-1234')
print("bool = " , bool1.pos)
bool2 = re.match(r'^\d{3}\-\d{3,8}$','010-122222233')
print("bool2 = ",bool2)

# match spilt string
result = re.split(r'\s+','a b   c')
print(result)

#cut string
m = re.match(r'^(\d{3})-(\d{3,8})$','010-1231212')
print(m)
print(m.group(1))
print(m.group(2))

#leagueGroup = re.match(u"([/u4e00-/u9fa5]+)","\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t[泰超]\r\n\t\t\t\t    \r\n\t\t\t\t\t")
xx=r'(\w+)'
pattern = re.compile(xx)
results =  pattern.findall("\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t[泰超]\r\n\t\t\t\t    \r\n\t")
print(results[0])

m2 = re.match(r'\D*(\d{1,4}\w)','\t\t\t\t\t86天')
print('m2 = = ' , m2.group(1))
print(m.groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')


print(re_telephone.match('010-12312').groups())

print(re_telephone.match("010-8982").groups())

myEail = r'[\w\.]+@\w+\.\w+'
val = "someone@gmail.com"
val2 = 'bill@gates@microsoft.com'
eail = re.match(myEail,val)
print('eail = ',eail.pos)
print(len(val2))

url = r'http://news.ifeng.com/a/\d+/\d+_\d\.shtml'
val_url = 'http://news.ifeng.com/a/20160422/48556097_0.shtml'
print('length = ',len(val_url))
result = re.match(url,val_url)
print("result.pos = ",result.endpos)
print(re.match(url,val_url))

match_url = 'http://8.wacai.com/list/wenying/\w\d+$';
url = 'http://8.wacai.com/list/wenying/p3';
res = re.match(match_url,url)
print(res.endpos)

resp_url = "http://wacai.com/list/wenying"
ma   =  re.search(r'([http:\/\/|https:\/\/].*\.\w+)',resp_url)
print(ma.group(1))

rs = ".com.com"
rs2 = re.match(r'\..*',rs)
print('rs2 = ',rs2)

rss = ' 7.0% ' \
      '~ 9.8% '
rs_ma = re.search(r'(\d+\.\d+\%).+~.+(\d+\.\d+\%)',rss)
print('rs_ma = ',rs_ma.lastindex)

objs = ['8.00%', '11.50%']
print(type(objs[0]+'~'+objs[1]))

html = '''
<p class="first"><a class="reference internal" href="../topics/spiders.html#scrapy.spiders.Spider.parse" title="scrapy.spiders.Spider.parse"><code class="xref py py-meth docutils literal"><span class="pre">parse()</span></code></a>: a method that will be called to handle
the response downloaded for each of the requests made. The response parameter
is an instance of <a class="reference internal" href="../topics/request-response.html#scrapy.http.TextResponse" title="scrapy.http.TextResponse"><code class="xref py py-class docutils literal"><span class="pre">TextResponse</span></code></a> that holds
the page content and has further helpful methods to handle it.</p>
<p>The <a class="reference internal" href="../topics/spiders.html#scrapy.spiders.Spider.parse" title="scrapy.spiders.Spider.parse"><code class="xref py py-meth docutils literal"><span class="pre">parse()</span></code></a> method usually parses the response, extracting
the scraped data as dicts and also finding new URLs to
follow and creating new requests (<a class="reference internal" href="../topics/request-response.html#scrapy.http.Request" title="scrapy.http.Request"><code class="xref py py-class docutils literal"><span class="pre">Request</span></code></a>) from them.</p>
</li>
<a href="http://www.xiaoniu88.com/product/financial/23">a</a>
</ul>
<a href="/finance/web/list?pageId=401&pageNo=3">  3 </a>
<a href="http://www.xiaoniu88.com/product/financial">a</a>
<div class="section" id="how-to-run-our-spider">
<h3>How to run our spider<a class="headerlink" href="#how-to-run-our-spider" title="Permalink to this headline">¶</a></h3>
<p>To put our spider to work, go to the project&#8217;s top level directory and run:</p>
<div class="highlight-default"><div class="highlight"><pre><span></span><span class="n">scrapy</span> <span class="n">crawl</span> <span class="n">quotes</span>
</pre></div>
</div>
'''

# obj = re.findall(r"http://www\.xiaoniu88\.com\/product/financial[/\d+]{0,}",html)
obj = re.findall(r"/finance/web/list\?pageId=\d+&pageNo=\d+",html)
print("obj = ",obj)


import json
try:
      jsonObj = json.loads(html)
      print(jsonObj)
except Exception as ex:
      print(ex)
# from scrapy import Selector
# obj = Selector(text=html)
# print(obj.xpath("//a/@href").extract())
# results = re.search(r'.*(http://www\.xiaoniu88\.com/product/financial/\d+$).*',
#                     "<a>http://www.xiaoniu88.com/product/financial</a>")
