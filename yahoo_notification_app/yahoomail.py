import cookielib, urllib2
import urllib
from bs4 import BeautifulSoup
import sys
import os
import dbus
import ConfigParser

a = os.path.join(sys.path[0], 'logo.jpg')
b = os.path.join(sys.path[0], 'config.ini')

Config = ConfigParser.ConfigParser()
Config.read(b)

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


Email = ConfigSectionMap("SectionOne")['email']
Password = ConfigSectionMap("SectionOne")['password']

LoginUrl="https://login.yahoo.com/config/login?"
ExportUrl="https://in-mg61.mail.yahoo.com/neo/b/launch?"
form_data = {'login':Email, 'passwd':Password}
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
item              = "org.freedesktop.Notifications"
path              = "/org/freedesktop/Notifications"
interface         = "org.freedesktop.Notifications"
app_name          = "Test Application"
id_num_to_replace = 0
icon              = a
title             = "Yahoo Mail"
text              = "You have %d unread mail in your yahoo account" % n
actions_list      = ''
hint              = ''
time              = 5000   # Use seconds x 1000

bus = dbus.SessionBus()
notif = bus.get_object(item, path)
notify = dbus.Interface(notif, interface)
notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, time)
