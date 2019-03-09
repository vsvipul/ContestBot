import sources.scrapper as scrapper
import json
from multiprocessing import Process
contestFile = 'contest.json'

def printToFile(contests):
    print(contests)
    for contest in contests:
        print(contest)
        contest['startTime'] = str(contest['startTime'])
        contest['endTime'] = str(contest['endTime'])
    with open(contestFile,'w') as outfile:
        json.dump(contests,outfile)

def readFromFile():
    with open(contestFile) as json_file:
        return json.load(json_file)

def searchInJSON(platform,startTime,endTime):
    contests = readFromFile()
    tempContests = []
    for contest in contests:
        if contest in platform:
            tempContests.append(contest)

if __name__ == "__main__":
    contests = scrapper.process()
    printToFile(contests)
    tempContests = readFromFile()
    print(tempContests)