import requests
from bs4 import BeautifulSoup


query = "Dog"
URL = "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
imgclass = soup.find_all("img", {"class": "t0fcAb"})
for a in imgclass:
    print(a['src'])
    response = requests.get(a['src'])
    file = open(query+".png", "wb")
    file.write(response.content)
    file.close()
    break #if You Want TO Download Multiplple Just remove Break Statement And Change The Name EVery Time 
