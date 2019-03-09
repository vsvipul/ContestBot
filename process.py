import sources.scrapper as scrapper
import json
from dateutil.parser import parse
from dateutil.tz import tzoffset
from datetime import datetime
import pytz
contestFile = 'contest.json'

def get_message(text,reply,platform):
    return text

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

if __name__ == "__main__":
    contests = scrapper.process()
    printToFile(contests)
    platform = ['CODECHEF']
    tempContests = searchInJSON(platform,datetime.now(tzoffset(None,19800)),0)
    print(platform,datetime.now(tzoffset(None,19800)))
    print(tempContests)

def get_message(msg , recipent_id , kiska):
    # get_context = Digflow(msg)
    get_context = ["Hackerearth" , "search"]
    if get_context[0] == "Hackerearth":
        if get_context[1] == "search":
            return do_what_i_say("HACKEREARTH")
        elif get_context[1] == "reminder":
            return set_reminder(get_context[2])
    if get_context[0] == "Codeforces":
        if get_context[1] == "search":
            return do_what_i_say("Codeforces")
        elif get_context[1] == "reminder":
            return set_reminder(get_context[2])
    if get_context[0] == "Codechef":
        if get_context[1] == "search":
            return do_what_i_say("Codechef")
        elif get_context[1] == "reminder":
            return set_reminder(get_context[2])

def set_reminder(data , name):
    #  do searching for related contest
    A = readFromFile()
    reply = None
    for con in A:
        if con["name"] == data["name"]:
            reply = con
            break
    reminder.apply_async((data, reply) , eta=datetime.now() + data["time"])    


def do_what_i_say(platfrom):
    M = []
    content = readFromFile()
    for con in content:
        if con["platform"] == platfrom:
            M.append(con)
    return M


def update_every_six_hour():
    A = scrapper.process()
    printToFile(A)



schedule.every(6).hour.do(update_every_six_hour)

while True:
    schedule.run_pending()
    time.sleep(1)


    
    
