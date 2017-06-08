#! /usr/bin/python3

# stopwatch.py - a simple stopwatch pgm
import time

print('Press Enter to Begin.Afterwars,press ENTER to :"click" the stopwatch press ctrl+c to quit')

input()
print('Started')
startTime=time.time()
lastTime=startTime
lapNum=1

try:
  while True:
    input()
    lapTime=round(time.time()-lastTime,2)
    totalTime=round(time.time()-startTime)
    print('Lap #%s: %s (%s)'%(lapNum,totalTime,lapTime),end='')
    lapNum+=1
    lastTime=time.time()
except KeyboardInterrupt:
  print('\n Done')
  
