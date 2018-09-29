from datetime import datetime,timedelta,timezone

now = datetime.now()
print(now)

dt = datetime(2016,3,2,13,40)
print(dt)
print("timestamp = ",dt.timestamp())
print(datetime.fromtimestamp(1429417200.0))
print((1456897200.0-1429417200.0)/(60*24))
print("string = ",now.strftime('%a , %b %d %H:%M'))

cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)

#datetime to str
print("string = ",now.strftime('%a , %b %d %H:%M'))

print(now+timedelta(hours=10,days=1))

print("\n\n#create time zone UTC+8:00")
tz_utc_8 = timezone(timedelta(hours=8)) #create time zone UTC+8:00

print(datetime.now())
dt = now.replace(tzinfo=tz_utc_8)
print("dt = ",dt)

print("\n\n 强制设置时区")
utc_dt = datetime.utcnow().replace(tzinfo=tz_utc_8)
print(utc_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

dts = {'www':1,'bbb':2}
print(dts.keys())

now = datetime.now()
print("now = ",now)
today_date    = now.strftime('%a, %b %d %H:%M')
print("today_date = ",today_date)

# parser = datetime.strptime('27 May 2015','%d %b %y')
# print('parser = ',parser)
timeStr = datetime.strftime(now,'%Y%m%d%H%M%S%s')
print("timeStr = " ,timeStr[:-4])