import sources.scrapper as scrapper
import json
from dateutil.parser import parse
from dateutil.tz import tzoffset
from datetime import datetime
import schedule
import pytz
import schedule
import time
import text
contestFile = 'contest.json'
list_platform = []

'''
todo : 
    make a final multprocessing file
    modify get_message
    make messenger.py and zulip.py more interactive
    correct the codechef randaap
 '''

def printToFile(contests):
    for contest in contests:
        contest['startTime'] = str(contest['startTime'])
        contest['endTime'] = str(contest['endTime'])
        contest['platform'] = contest['platform'].upper()
    with open(contestFile,'w') as outfile:
        json.dump(contests,outfile)

def readFromFile():
    contests = []
    with open(contestFile) as json_file:
        contests = json.load(json_file)
        for contest in contests:
            contest['startTime'] = parse(contest['startTime'])
            contest['endTime'] = parse(contest['endTime'])
        return contests

def searchInJSON(platform,startTime,endTime):
    contests = readFromFile()
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
    # get_context = Digflow(msg)
    # get_context = ["Hackerearth" , "search"]
    # if get_context[0] == "Hackerearth":
    #     if get_context[1] == "search":
    #         return do_what_i_say("HACKEREARTH")
    #     elif get_context[1] == "reminder":
    #         return set_reminder(get_context[2])
    # if get_context[0] == "Codeforces":
    #     if get_context[1] == "search":
    #         return do_what_i_say("Codeforces")
    #     elif get_context[1] == "reminder":
    #         return set_reminder(get_context[2])
    # if get_context[0] == "Codechef":
    #     if get_context[1] == "search":
    #         return do_what_i_say("Codechef")
    #     elif get_context[1] == "reminder":
    #         return set_reminder(get_context[2])

    ans = []

    for i range(len(msg['platform'])):
        if msg['platform'][i] == 'codeforces':
            ans.append(do_what_i_say("Codeforces"))

        elif msg['platform'][i] == 'hackerearth':
            ans.append(do_what_i_say("HACKEREARTH"))

        elif msg['platform'][i] == 'codechef':
            ans.append(do_what_i_say("Codechef"))

    return ans

def helper(msg , recipent_id , kiska):
    list_platform = text.get_response(msg)

    if type(out) is not dict:
        return out

    else:
        get_message(out,recipent_id , kiska)

        



def set_reminder(data, recipent_id, kiska):
    #  do searching for related contest
    A = readFromFile()
    delay = data["delay"]
    reply = None
    for con in A:
        if con["name"] == data["name"]:
            reply = con
            break
    reminder.apply_async((kiska, reply, recipent_id) , countdown=delay)    


def do_what_i_say(platfrom):
    M = []
    content = readFromFile()
    print(content)
    for contest in content:
        if contest['platform'] == platfrom:
            M.append(contest)
    F = process_contests(M)
    return F


def update_every_six_hour():
    A = scrapper.process()
    printToFile(A)

def process_contests(contests):
    idx = 0
    arr = []
    for contest in contests:
        arr.append(str(idx+1) + '. ' + contest['name'] + ' on ' + contest['platform'] + ' starting at ' + str(contest['startTime']) + ' and ending at ' + str(contest['endTime']) + '. Register at [link](' + contest['link'] + ').\n')
        idx+=1
    return arr



def ini():
    update_every_six_hour()
    schedule.every(6).hours.do(update_every_six_hour)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    ini()
