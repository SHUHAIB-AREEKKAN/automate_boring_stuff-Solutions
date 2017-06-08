#! /usr/bin/python3
# need tweaking beacuse aftre compose of mail sometime it will not able to
#find the desired of receipent and subject and mail body.but most time works
#This files take input of email id from cmd and ..\
# send a mail to the argument
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gmail_send(argu,sub,cont):
  browser=webdriver.Firefox()
  browser.get('https://mail.google.com')
  emailElem=browser.find_element_by_id('Email')
  emailElem.send_keys('shaz3606@gmail.com')
  emailElem.submit()
 # wait=WebDriverWait(browser,20)
 # passElem=browser.find_element_by_id('Passwd')
  wait=WebDriverWait(browser,20)
  passElem=wait.until(EC.visibility_of_element_located((By.ID,"Passwd")))
  passElem.clear()
  passElem.send_keys('shuhaib_10')
  passElem.submit()
  wait2=WebDriverWait(browser,10)
  #compElem=browser.find_element_by_class_name('T-I-KE')
  compElem=wait2.until(EC.visibility_of_element_located((By.CLASS_NAME,"T-I-KE")))
  compElem.click()
  recElem=wait.until(EC.visibility_of_element_located((By.ID,":b0")))
  recElem.clear()
  recElem.send_keys(argu)
  subElem=wait.until(EC.visibility_of_element_located((By.ID,":ak")))
  subElem.clear()
  subElem.send_keys(sub)
  contElem=wait.until(EC.visibility_of_element_located((By.ID,":bp")))
  contElem.clear()
  contElem.send_keys(cont)
  sendBut=wait.until(EC.visibility_of_element_located((By.ID,":aa")))
  sendBut.click()
  print('done') 

if sys.argv[1]:
  print('Submitting Email')
  gmail_send(sys.argv[1],sys.argv[2],sys.argv[3])
else:
  print("not the option")


