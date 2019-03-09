import requests
import json

def codeforces():
    output = requests.get("http://codeforces.com/api/contest.list?gym=false").json()['result']
    
    idx = 0
    for i in range(len(output)):
        
        if output[i]['phase'] != "BEFORE":
            break

        idx += 1

    future_contests = output[:idx]

    future_contests = json.dumps(future_contests)
    
    return future_contests
    