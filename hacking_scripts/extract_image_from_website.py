import requests
from bs4 import BeautifulSoup
import urllib

'''
Author: Anthoniraj Amalanathan
Date Last Modified: 21-Mar-2023
Description: This Script will download ALL images from the given URL
'''

url = "https://example.com/" # Replace this with the website's URL.
getURL = requests.get (url, headers= { "User-Agent": "Mozilla/5.0" })
if getURL.status_code:
    soup = BeautifulSoup(getURL.content, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        img_url = image['src']
        filename = img_url.split("/")[-1]
        urllib.request.urlretrieve(img_url, "images/"+filename)
        print("Downloaded: "+img_url)
else:
    print("Website Unavailable")