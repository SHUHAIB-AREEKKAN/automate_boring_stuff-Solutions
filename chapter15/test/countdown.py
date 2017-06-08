#! /usr/bin/python3
#countdown.py - A simple count down script

import time,subprocess

timeLeft=5
while timeLeft>0:
  print(timeLeft,end='')
  time.sleep(1)
  timeLeft-=1
  

subprocess.Popen(['see','alarm.wav'])
