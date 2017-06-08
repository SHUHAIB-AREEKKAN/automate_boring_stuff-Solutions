#! /usr/bin/python3

# 2048_game.py will randomly gives input to 2048 game which is in online

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def some_keys():
  browser=webdriver.Firefox()
  browser.get('https://gabrielecirulli.github.io/2048/')
  htmlElem=browser.find_element_by_tag_name('html')
  a=0
  
  while True:
    a=random.randint(1,4)
    if a==1:
      htmlElem.send_keys(Keys.UP)
    elif a==2:
      htmlElem.send_keys(Keys.DOWN)
    elif a==3:
      htmlElem.send_keys(Keys.RIGHT)
    elif a==4:
      htmlElem.send_keys(Keys.LEFT)
    else:
      print("not a desired option")
   

some_keys()
