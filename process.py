import sources.scrapper as scrapper
import json
from multiprocessing import Process
contestFile = 'contest.json'

def printToFile(contests):
    for contest in contests:
        contest['startTime'] = str(contest['starttime'])
        contest['endTime'] = str(contest['endTime'])
    with open(contestFile,'w') as outfile:
        json.dump(contests,outfile)

def readFromFile():
    with open(contestFile) as json_file:
        return json.load(json_file)
    
if __name__ == "__main__":
    contests = scrapper.process()
    printToFile(contests)
    tempContests = readFromFile()
    print(tempContests)