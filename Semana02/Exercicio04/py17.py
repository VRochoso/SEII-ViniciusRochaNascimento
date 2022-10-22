import datetime

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000000000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dttoday = datetime.datetime.today()
dtnow = datetime.datetime.now()
dtutcnow = datetime.datetime.utcnow()
print(dttoday)
print(dtnow)
print(dtutcnow)

import pytz
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dtnow = datetime.datetime.now(tz=pytz.UTC)
print(dtnow)

dtutcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dtutcnow)

dtmtn = dtutcnow.astimezone(pytz.timezone('US/Mountain'))
print(dtmtn)

for tz in pytz.all_timezones:
    print(tz)

dtmtn = datetime.datetime.now()
mtntz = pytz.timezone('US/Mountain')
dtmtn = mtntz.localize(dtmtn)
dteast = dtmtn.astimezone(pytz.timezone('US/Eastern'))
print(dteast)
print(dtmtn)

dtmtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dtmtn.isoformat())
print(dtmtn.strftime('%B %d %Y'))

dtstr = 'july 26, 2016'
dt = datetime.datetime.strptime(dtstr, '%B %d %Y')
print(dt)