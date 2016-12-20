from xml.parsers.expat import ParserCreate
from datetime import datetime,timedelta
from urllib import request

content = {}
today   = {}
tomorrow= {}
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print(attrs.keys())
        if 'city' in attrs.keys():
            content['city'] = attrs.get('city')
        if 'country' in attrs.keys():
            content['country'] = attrs.get('country')
        if 'day' in attrs.keys():
            now = datetime.now()
            today_date    = now.strftime("%a")
            tomorrow_date = (now+timedelta(days=1)).strftime("%a")
            if today_date == attrs['day']:
                today['text'] = attrs['text']
                today['low']  = attrs['low']
                today['high'] = attrs['high']
            elif tomorrow_date == attrs['day']:
                tomorrow['text'] = attrs['text']
                tomorrow['low']  = attrs['low']
                tomorrow['high'] = attrs['high']
    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#" version="2.0">
<channel>
<title>Yahoo! Weather - Beijing, CN</title>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Beijing__CN/*http://weather.yahoo.com/forecast/CHXX0008_c.html
</link>
<description>Yahoo! Weather for Beijing, CN</description>
<language>en-us</language>
<lastBuildDate>Thu, 03 Mar 2016 1:59 pm CST</lastBuildDate>
<ttl>60</ttl>
<yweather:location city="Beijing" region="" country="China"/>
<yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
<yweather:wind chill="12" direction="90" speed="6.44"/>
<yweather:atmosphere humidity="45" visibility="1.4" pressure="1011" rising="0"/>
<yweather:astronomy sunrise="6:44 am" sunset="6:08 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>
http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
</url>
</image>
<item>
<title>Conditions for Beijing, CN at 1:59 pm CST</title>
<geo:lat>39.91</geo:lat>
<geo:long>116.39</geo:long>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Beijing__CN/*http://weather.yahoo.com/forecast/CHXX0008_c.html
</link>
<pubDate>Thu, 03 Mar 2016 1:59 pm CST</pubDate>
<yweather:condition text="Haze" code="21" temp="12" date="Thu, 03 Mar 2016 1:59 pm CST"/>
<description>
<![CDATA[
<img src="http://l.yimg.com/a/i/us/we/52/21.gif"/><br /> <b>Current Conditions:</b><br /> Haze, 12 C<BR /> <BR /><b>Forecast:</b><BR /> Thu - Partly Cloudy. High: 17 Low: 1<br /> Fri - Mostly Cloudy. High: 16 Low: 2<br /> Sat - Sunny/Wind. High: 13 Low: -3<br /> Sun - Partly Cloudy. High: 13 Low: -3<br /> Mon - Sunny. High: 14 Low: -1<br /> <br /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Beijing__CN/*http://weather.yahoo.com/forecast/CHXX0008_c.html">Full Forecast at Yahoo! Weather</a><BR/><BR/> (provided by <a href="http://www.weather.com" >The Weather Channel</a>)<br/>
]]>
</description>
<yweather:forecast day="Thu" date="3 Mar 2016" low="1" high="17" text="Partly Cloudy" code="30"/>
<yweather:forecast day="Fri" date="4 Mar 2016" low="2" high="16" text="Mostly Cloudy" code="28"/>
<yweather:forecast day="Sat" date="5 Mar 2016" low="-3" high="13" text="Sunny/Wind" code="24"/>
<yweather:forecast day="Sun" date="6 Mar 2016" low="-3" high="13" text="Partly Cloudy" code="30"/>
<yweather:forecast day="Mon" date="7 Mar 2016" low="-1" high="14" text="Sunny" code="32"/>
<guid isPermaLink="false">CHXX0008_2016_03_07_7_00_CST</guid>
</item>
</channel>
</rss>
'''
pasr = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = pasr.start_element
parser.EndElementHandler = pasr.end_element
parser.CharacterDataHandler = pasr.char_data
# f = request.urlopen('http://weather.yahooapis.com/forecastrss?u=c&w=2142699')
# xml1 = f.read()
parser.Parse(xml)
content['today'] = today
content['tomorrow'] = tomorrow

print(content)