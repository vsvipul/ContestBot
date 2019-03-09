import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup

def codechef():
    url = "https://www.codechef.com/contests"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib') 
    arr = []
    table = soup.find_all('table', {"class":"dataTable"})[1].tbody.findAll('tr')

    for item in table:
        obj = {}
        tds = item.findAll('td')
        obj['link'] = 'https://www.codechef.com' + tds[1].contents[0]['href']
        obj['name'] = tds[1].contents[0].text
        obj['startTime'] = parse(tds[2]['data-starttime'])
        obj['endTime'] = parse(tds[3]['data-endtime'])
        obj['platform'] = 'codechef'
        arr.append(obj)

    print(arr)
    return arr

codechef()