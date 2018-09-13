import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://goamiroo.com/collections/a-to-z-products/products/white-lace-bra-set-1-2-cup-hollow-out-brassiere-see-through-bra-transparent-lingerie-women-plus-size-sexy-underwear-sets')
soup = BeautifulSoup(page.text, 'html.parser')
#optiontitles = [i.string for i in soup.select(".main-product-select label")]

#optionvalues = [[w.string for w in i.select("option")] for i in soup.select(".single-option-selector")]

#new = zip(optiontitles,optionvalues)
#print(optiontitles)
#print(optionvalues)
#print(new)


for i in soup.select(".main-product-select"):
    optiontitle = i.find("label").string.strip()
    for w in i.select("option"):

        print([optiontitle,w.string])

