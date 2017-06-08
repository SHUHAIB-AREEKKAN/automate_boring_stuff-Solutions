import requests, os, bs4



str2=[]
str3=''

url = 'http://xkcd.com/1745' # starting url
try:

  if os.path.isfile('a.txt'): 
    f=open('a.txt','r')
    str2=f.readlines()
    url=str2[0].strip()
    
    
    

except FileNotFoundError:
  print('File Not found')
   
  


os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        file_obj=open('a.txt','w')
        file_obj.write(url)
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the "Prev" button's url.
    prevLink = soup.select('a[rel="next"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')

