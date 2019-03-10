import sources.scrapper as scrapper
import json
from dateutil.parser import parse
from dateutil.tz import tzoffset
from datetime import datetime
import schedule
import pytz
import time
import text
from celery_tasks import reminder

contestFile = 'contest.json'
list_platform = []
tempGB = {}
reminder_file = 'reminder.json'


def printToString(contest,filename):
    with open(filename,'w') as outfile:
        json.dump(contest,outfile)


def printToFile(contests, filename):
    # print(contests)
    # print('++++++++++++++++++'+filename)
    for contest in contests:
        contest['startTime'] = str(contest['startTime'])
        contest['endTime'] = str(contest['endTime'])
        contest['platform'] = contest['platform'].upper()
    with open(filename,'w') as outfile:
        json.dump(contests,outfile)


def readFromString(file_name):
    contests = []
    with open(file_name) as json_file:
        contests = json.load(json_file)
        return contests


def readFromFile(file_name):
    contests = []
    with open(file_name) as json_file:
        contests = json.load(json_file)
        for contest in contests:
            contest['startTime'] = parse(contest['startTime'])
            contest['endTime'] = parse(contest['endTime'])
        return contests


def searchInJSON(platform,startTime,endTime):
    contests = readFromFile(contestFile)
    tempContests = []
    for contest in contests:
        if contest['platform'] in platform:
            tempContests.append(contest)
    contests = tempContests
    tempContests = []
    if startTime:
        for contest in contests:
            if contest['startTime']>= startTime:
                tempContests.append(contest)
        contests = tempContests
        tempContests = []
    if endTime:
        for contest in contests:
            if contest['startTime']<= endTime:
                tempContests.append(contest)
        contests = tempContests
    return contests


def get_message(msg , recipent_id , kiska):
    ans = []
    idx = 0

    for i in range(len(msg['platform'])):
        if msg['platform'][i] == 'codeforces':
            ans = ans + (do_what_i_say("CODEFORCES"))

        elif msg['platform'][i] == 'hackerearth':
            ans = ans + (do_what_i_say("HACKEREARTH"))

        elif msg['platform'][i] == 'codechef':
            ans = ans + (do_what_i_say("CODECHEF"))

    ans2 = []
    for i in ans:
        ans2.append(str(idx+1)+'. '+i)
        idx+=1

    temp = ans2
    # print(ans)
    printToString(ans, reminder_file)
    return temp


def helper(msg , recipent_id , kiska):

    # print('IN HELPER')
    # print("msg" + msg)

    if 'reminder' in msg:
        idx = text.get_response(msg)
        # print(idx)
        return set_reminder(idx,recipent_id,kiska)
    
    list_platform = text.get_response(msg)
    # print(list_platform)
    # print("It was a platform")
    if type(list_platform[0]) is not dict:
        return list_platform
    else:
        temp = get_message(list_platform[0],recipent_id , kiska)
        # print('----------------')
        # print(temp)
        return temp
        


def set_reminder(index, recipent_id, kiska):
    #  do searching for related contest
    if len(index) == 0:
        return ["nothing set"]

    A = []
    try:
        sent_data = readFromString(reminder_file)
    except:
        print("File Doesn't Exist")
        return ["unknown"]

    for i in index:
        # reply = process_contests(data[int(i)-1])
        reply = sent_data[i-1]
        try:
            date = (tempGB[sent_data[i-1]] - datetime.now()) 
            delay = date.seconds + date.days*60*60*24 
            reminder.apply_async((kiska, reply, recipent_id) , countdown=delay)
        except:
            pass
    return ["Reminder has been set!"]


def do_what_i_say(platfrom):
    M = []
    content = readFromFile(contestFile)
    print(content)
    for contest in content:
        if contest['platform'] == platfrom:
            M.append(contest)
    F = process_contests(M)
    return F

def gettimeleft_cc(time):
	data = re.findall("\d+",time);
	data = list(map(int,data));
	timeleft=(datetime.datetime.strptime(time,"%d %b %Y\n%H:%M:%S")-datetime.datetime.utcnow()).total_seconds();
	return timeleft-330*60;


def update_every_six_hour():
    A = scrapper.process()
    printToFile(A , contestFile)


def process_contests(contests):
    idx = 0
    arr = []
    for contest in contests:
        temp = contest['name'] + ' on ' + contest['platform'] + ' starting at ' + str(contest['startTime']) + ' and ending at ' + str(contest['endTime']) + '. Register at [link](' + contest['link'] + ').\n'
        idx+=1
        tempGB[temp] = contest['startTime']
        arr.append(temp)
    return arr


def ini():
    update_every_six_hour()
    schedule.every(6).hours.do(update_every_six_hour)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    ini()
