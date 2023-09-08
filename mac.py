# -*- coding: UTF-8 -*-
# get json data from a url, and speak it every 5 sec.
# tested with mac 11.4,  python 2.7
# AUTHOR: INCENSING PANDA @ 2023

import urllib2
from os import system
import time, json


def get_and_read():
  link = ""
  f = urllib2.urlopen(link)
  info = json.loads(f.read())
  f.close()
  print(info)
  return info["es"] % 100


last = 0
while 1:
 num = get_and_read()
 if last != num:
     system("say -v Mei-Jia '[[pbas -6]]' " + str("{:.1f}".format(num)).replace(".","点"))
     last = num
 time.sleep(5)
