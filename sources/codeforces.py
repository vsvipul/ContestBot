import requests
from datetime import datetime,timedelta
from dateutil.parser import parse

cur = datetime.now()
def codeforces():
    output = requests.get("http://codeforces.com/api/contest.list?gym=false").json()['result']
    
    future_contests = []
    for i in range(len(output)):
        
        if output[i]['phase'] != "BEFORE":
            break

        temp = {}
        temp['link'] = "https://codeforces.com/contest/" + str(output[i]['id'])
        temp['name'] = output[i]['name']

        temp['startTime'] = cur + timedelta(seconds=-output[i]['relativeTimeSeconds'])
        temp['endTime'] = temp['startTime'] + timedelta(seconds=output[i]['durationSeconds'])
        temp['platform'] = 'Codeforces'
        # print(temp['startTime'],temp['endTime']) 

        future_contests.append(temp)

    # future_contests = json.dumps(future_contests)
    
    return future_contests
    