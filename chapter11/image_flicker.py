#! /usr/bin/python3

#imageflickr.py download images from flickr for desired search result


import sys,os,requests,bs4,re

from selenium import webdriver

url_term='https://www.flickr.com/search/?text='

os.makedirs('Flickr_Download',exist_ok=True)
def flick_image(argu):
  real_links=[]
  res=requests.get(url_term+argu)
  res.raise_for_status()
  soup=bs4.BeautifulSoup(res.text)
  #print(soup)
  imageId=soup.findAll("div",{"class":"view photo-list-photo-view requiredToShowOnServer awake"})
  ss=str(imageId)
  regex=re.findall(r'([a-z\-_0-9\/\:\.]*\.(jpg|jpeg|png|gif))',ss) 
  for i in regex:
    (my,waste)=i
    real_links.append(my[2:])
  print("Starting The Download")
  i=0
  for sd in real_links:
    print(sd)
    rs='http://'+sd
    res1=requests.get(rs)
    res1.raise_for_status()
    imagefile=open(os.path.join('Flickr_Download',str(i)),'wb')
    i=i+1
    for chunk in res1.iter_content(100000):
      imagefile.write(chunk)
    imagefile.close()     


flick_image('flowers') 



  
