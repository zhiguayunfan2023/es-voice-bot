#!/usr/bin/python
# -*- coding: UTF-8 -*-

# -*- coding: UTF-8 -*-
# get json data from a url, and speak it every 5 sec.
# tested with python 3.x
# AUTHOR: INCENSING PANDA @ 2023


from os import system
import time, json, decimal, ssl
import urllib.request


def get_and_read2(n):
  link = ""
  context = ssl._create_unverified_context()
  with urllib.request.urlopen(link,context=context) as f:
    info = json.loads(f.read())
    print(info)

  num = "{:.1f}".format(info["es"] % 100)
  if num != n:
    system("say -v Mei-Jia '[[pbas -200]]' " + num.replace(".", "点"))
  return num
 
n = 0.0
while 1:
  n = get_and_read2(n)
  time.sleep(5)
