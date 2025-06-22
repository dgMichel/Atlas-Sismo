import requests 
from bs4 import BeautifulSoup
import os 

url="https://www.cenais.gob.cu/cenais/?page_id=1131"
lista=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
count=11
alter=13
r=requests.get(url)
b=BeautifulSoup(r.text,"html.parser")

for i in b.find("article",class_="post-1131 page type-page status-publish hentry").find("div", class_="wp-block-columns is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex").find_all("p"):
    x=i.find('a')
    if x is not None:
        if x["href"][0]=="/":
            url="https://www.cenais.gob.cu"+x["href"]
        else:
            url=x["href"]
        if("www.cenais.cu") in url:
            url=url.replace("www.cenais.cu","www.cenais.gob.cu")
        if("http:/") in url:
            url=url.replace("http:/","https:/")
        url=url.replace(" ","%20")
        data=requests.get(url)
        if("2015" in url):
            with open(f"PDF/Mensual/{alter}.pdf","wb") as f:
                f.write(data.content)
            alter+=1
        elif "(OCTUBRE-NOVIEMBRE)" in url:
            with open(f"PDF/Mensual/Octubre_Noviembre2018.pdf","wb") as f:
                f.write(data.content)
            count=8
        elif "Enero%20y%20Febrero" in url:
            with open("PDF/Mensual/Enero_Febrero2018.pdf","wb") as f:
                f.write(data.content)
            count=11
        elif "Enero" in url:
            with open(f"PDF/Mensual/Enero{url[-8:]}","wb") as f:
                f.write(data.content)
            count=11
        else:
            with open(f"PDF/Mensual/{lista[count]+url[-8:]}","wb") as f:
                f.write(data.content)
            count-=1
        
        
    

