import sys
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

content = input("Enter the topic about which you would want to know more ")
URL = "https://en.wikipedia.org/wiki" + content
from lxml import etree

response = urlopen(URL)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
xpathselector = "/html/body/div[3]/div[3]"
p = tree.xpath(xpathselector)
print(p)
