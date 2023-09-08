# ref: https://stackoverflow.com/questions/31167967/python-3-4-text-to-speech-with-sapi
# get json data from a url, and speak it every 5 sec.
# tested with windows 11, python 3.9
# AUTHOR: INCENSING PANDA @ 2023

import urllib.request,win32com.client
import time, json


def get_and_read():
  link = ""
  with urllib.request.urlopen(link) as f:
    info = json.loads(f.read())
    print(info)
    return info["es"] % 100


speaker = win32com.client.Dispatch("SAPI.SpVoice")

last = 0
while 1:
 num = get_and_read()
 if num != last:
   speaker.Speak("{:.1f}".format(num))
   last = num
 time.sleep(5)
