import requests
import json
from requests_html import HTMLSession
import time

class Tracker:
    """
    Docs: 
        https://requests.readthedocs.io/projects/requests-html/en/latest/
    """
    
    def __init__(self, state):
        self.state = state
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.search = []
        self.url = "https://%s.olx.com.br/" % self.state
        
        self.produtos = []
        

    def GetProducts(self, product, pages):
        session = HTMLSession()
        productString = product
        for page in range(pages):
            page += 1
            print(page)
            if page == 1:
                queryUrl = self.url + "?q=" + productString + "&sf=1"
            else:
                querry = "?o={}&q={}&sf=1".format(page, productString)

                queryUrl = self.url + querry
                
            rt = session.get(queryUrl)
            print(rt.html)
            htmlItems = rt.html.find(".sc-1fcmfeb-2")
            print(htmlItems)
            for item in htmlItems:
                tag = item.find(".fnmrjs-0", first = True)
                if tag != None:
                    #title
                    title = tag.attrs['title']

                    #price
                    priceTag = tag.find(".hLiLwY", first = True)
                    if priceTag.text == '':
                        print("Text vazio")
                        price = float(0)
                    else:
                        priceValue = priceTag.text
                        price = priceValue.replace('.', '')
                        price = float(price[3:])
                    
                    #imgUrl
                    imgUrl = tag.find("img", first = True).attrs["src"]
                    
                    #location
                    location = tag.find(".fVmnUX", first = True ).text
                    print(location)

                    #url
                    url = tag.attrs['href']
                    print(url)

                    #id
                    code = tag.attrs['data-lurker_list_id']
                    print(code)
                    
                    productOutput = {
                        "title":    title,
                        "location": location,
                        "price":    price,
                        "url":      url,
                        "id":     code,
                        "img":      imgUrl,
                    }

                    self.produtos.append(productOutput)

        return self.produtos
    
# MAIN
if __name__ == "__main__":
    track = Tracker("se")
    procura = input("O que voce Procura?")
    #track.search = [procura]
    #print(track.search)
    #while(True):
    track.GetProducts(procura, 10)
    
    #track.ConvertPrice("R$ 18.900", int)


"""
    [
        {
            title: "bla bla bla"
            price: 1000,
            code: 773901119,
            url: https://se.olx.com.br/sergipe/computadores-e-acessorios/processador-g2030-1155-773901119
        }
    ]
"""