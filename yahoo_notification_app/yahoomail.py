import cookielib, urllib2
import urllib
LoginUrl="https://login.yahoo.com/config/login?"
ExportUrl="http://mail.yahoo.com/"
form_data = {'login':'example@yahoo.com/in', 'passwd':'your password'}
form_data = urllib.urlencode(form_data)
jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
resp = opener.open(LoginUrl, form_data)
resp = opener.open(ExportUrl)
page = resp.read()

