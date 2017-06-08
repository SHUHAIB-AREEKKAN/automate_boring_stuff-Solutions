#! /usr/bin/python3
# downloadXkcd,py download every single XKCD comics with soup,requests

import requests,os,bs4

url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
  #download the page
  print('Downloading page %s..' %url)
  res=requests.get(url)
  res.raise_for_status()
  soup=bs4.BeautifulSoup(res.text)
  # finding url of comic
  comicElem=soup.select('#comic img')
  if comicElem == []:
    print("comic not found ")
  else:
    try:
      comicUrl='http:'+comicElem[0].get('src') 
      print('Downloading image %s...'%(comicUrl))
      res=requests.get(comicUrl)
      res.raise_for_status()
    except requests.exceptions.MissingSchema:
      #skip this comic
      prevLink=soup.select('a[rel="prev"]')[0]
      print(prevLink)
      url=url+prevLink.get('href')
      print(url)
      continue
      
