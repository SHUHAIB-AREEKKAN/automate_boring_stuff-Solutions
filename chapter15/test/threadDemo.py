import threading,time


print('Start of Program')
def takeNap():
  time.sleep(5)
  print('Wake Up!')


threadobj=threading.Thread(target=takeNap)
threadobj.start()

print('End of pgm')
