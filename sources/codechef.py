import requests
from bs4 import BeautifulSoup

url = "https://www.codechef.com/contests"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify())