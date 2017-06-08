#! /usr/bin/python3
# link_verification.py will be retrive all links in website and check all are   # working or not 

import sys,requests,bs4

def link_checker(link_pr):
  links_to=[]
  res=requests.get(link_pr)
  res.raise_for_status()
  soup=bs4.BeautifulSoup(res.text)
  for link in soup.findAll('a',href=True):
    links_to.append(link['href'])
  for check in links_to:
    try:
      res1=requests.get(check)
      res1.raise_for_status()
    except Exception as exc:
      print('404 ERROR')



link_checker('http://google.co.in')

    
  
  
