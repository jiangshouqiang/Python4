import re
from datetime import datetime , timezone,timedelta

def to_timestamp(dt_str,tz_str):
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    zones = timezone(timedelta(hours=7))
    zone_dt = dt.replace(tzinfo=zones)
    assert zone_dt.timestamp() == 1433121030.0,zone_dt

while True:
    dt_str = input("Input date string:")
    if re.match(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}',dt_str) :
        break
while True:
    tz_str = input("Input time zone string:")
    if re.match(r'UTC\+\d:\d{2}',tz_str) :
        tz_str = re.match(r'(\w+)(\+)(\d)(:\d{1,2})',tz_str).group(3)
        break
to_timestamp(dt_str,tz_str)