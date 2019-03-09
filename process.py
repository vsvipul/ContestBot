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