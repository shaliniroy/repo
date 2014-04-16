import cookielib, urllib2
import urllib
from bs4 import BeautifulSoup
import pynotify

LoginUrl="https://login.yahoo.com/config/login?"
ExportUrl="https://in-mg61.mail.yahoo.com/neo/b/launch?"
form_data = {'login':'example@yahoo.com/in', 'passwd':'your password'}
form_data = urllib.urlencode(form_data)
jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
resp = opener.open(LoginUrl, form_data)
resp = opener.open(ExportUrl)
page = resp.read()
soup = BeautifulSoup(page)
n = soup.em.b.string
n = str(n)
n = n.split(')')[0].lstrip('(')
n = int(n)
title = "Notification"
text  = "You have %d unread mail in your yahoo account" % n
pynotify.init("Test Application")
notification = pynotify.Notification(title, text)
notification.set_urgency(pynotify.URGENCY_NORMAL)
notification.show()


