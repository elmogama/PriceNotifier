from genericpath import exists
from bs4 import BeautifulSoup
import requests, re

def get_link_data():
    items_Data = []
    urls = []
    max_Prices = []

    # Check if links file exists
    if(exists("links.txt")):
        # Read each urls and info line in links file
        with open("links.txt", "r") as f:
            links_Lines = f.readlines()
            for url_Line in links_Lines:
                urls.append(url_Line.split("^")[0])
                max_Price = [url_Line.split("^")[1]]
                # .split() returns a list so we call the first 
                # element of that list in max_Price
                max_Prices.append(max_Price[0])

        # Go through each url and compare info retrieved
        # with the info entered by user
        for url, max_Price in zip(urls, max_Prices):
            # Instantiate max price entered by user
            max_Price = float(max_Price)

            in_Price_Range = False

            # Header to allow access to most sites
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
            result = requests.get(url, headers=headers).content
            doc  = BeautifulSoup(result, "html.parser")

            company_Site = (url.split(".com")[0].split("www.")[1]).lower()

            # Check if website is www.newegg.com
            if(company_Site == "newegg"):
                # Get the name of the item
                item_Name = doc.find(class_ = "product-title").string

                # Get the price of the item
                item_Price_Tag = doc.find(class_ = "price-current")
                listed_Dollar_Price = item_Price_Tag.strong.string
                listed_Cent_Price = item_Price_Tag.sup.string
                item_Price = listed_Dollar_Price + listed_Cent_Price
                item_Price = item_Price.replace(",", "")

            # Check if website is www.microcenter.com
            elif(company_Site == "microcenter"):

                # Get the name of the item
                item_Name = doc.find("span", attrs= {"class": re.compile("^ProductLink_.*")})["data-name"]

                # Get the price of the item
                item_Price_Tag = doc.find("span", {"id": "pricing"})
                item_Price = item_Price_Tag["content"]
                item_Price = item_Price.replace(",","")

            # Convert item price to float, if possible
            if(type(float(item_Price)) == float):
                item_Price = float(item_Price)
            else:
                item_Price = "Out Of Stock"

            # Determine if price of item is a number and is less than max price
            if(type(item_Price) == float and item_Price <= max_Price):
                in_Price_Range = True

            item_Data = [item_Name, item_Price, max_Price, in_Price_Range]
            items_Data.append(item_Data)

    else:
        print("Error: File \"links.txt\" not found")

    return items_Data