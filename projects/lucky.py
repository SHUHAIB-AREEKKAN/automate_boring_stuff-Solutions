#! /usr/bin/python3
#luck.py -open several tabs Google search results.

import requests,sys,webbrowser,bs4

print("GOOGLING ..")
res=requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
linkElems=soup.select('.r a')
#print(linkElems)
numopen=min(5,len(linkElems))
for i in range(numopen):
  webbrowser.open('http://google.com'+linkElems[i].get('href'))


