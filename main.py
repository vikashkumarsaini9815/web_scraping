# if you want to Scrape a website
# (1) use the API 
# (2) HTML web scraping useing same tool like bs4

# 1 Step : - install all requirements

# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://w3school.com"



# 2 Step : - Get the HTML

r = requests.get(url)
htmlcontent = r.content
# print(htmlcontent)

# 3 Step : - parse the HTML

soup = BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify())