
import requests
from bs4 import BeautifulSoup
import csv

pageList = ['https://goamiroo.com/collections/best-sellers?page=' + str(i) for i in range(1,91)]
print(pageList)
with open(r"/Users/adamwong/Documents/webscrape.csv", "w+", newline='', encoding='utf-8') as f:
    with open(r"/Users/adamwong/Documents/Options.csv", "w+", newline='', encoding='utf-8') as q:
        csvWriter = csv.writer(f)
        optionwriter = csv.writer(q)
        for i in range(len(pageList)):
            page = requests.get(pageList[i])
            page.encoding='utf-8'
            soup = BeautifulSoup(page.text,'html.parser')
            for link in soup.select('h5 a'):
                if link.has_attr('href') and 'collections/best-sellers/products' in link['href']:
                    print('https://goamiroo.com' + link['href'])
                    productPage = requests.get('https://goamiroo.com' + link['href'])
                    productPage.encoding = 'utf-8'
                    productSoup = BeautifulSoup(productPage.text, 'html.parser')
                    productName = productSoup.h3.string
                    description = productSoup.select(".main-product-description-product")[0].contents
                    productImages = [i['src'][2:] for i in productSoup.select("#carousel img")]
                    ProductSKU = str(i) + str(5000 + soup.find_all('a').index(link))
                    info = [ProductSKU, productName, productImages, description]
                    b = []
                    for we in info:
                        if isinstance(we, list):
                            for number in we:
                                b.append(number)
                        else:
                            b.append(we)
                    csvWriter.writerow(b)
                    try:
                        for i in soup.select(".main-product-select"):
                            optiontitle = i.find("label").string.strip()
                            for w in i.select("option"):
                                optionwriter.writerow([ProductSKU, optiontitle, w.string])


                    except:
                        pass

                    f.flush()
