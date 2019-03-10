
from celery import Celery
from celery.schedules import crontab
from datetime import datetime,timedelta
from pymessenger.bot import Bot
import zulip
client = zulip.Client(config_file="zuliprc")
ACCESS_TOKEN = 'EAALxONaYePsBAM5oBExC3ZC9yFGVucIiZB7fxP00AKhZBc9gjPZAqtk7Ed8T8UlD8bhZBsA8pWIcSpPrGpItvUSEk1ZAMPfZBr6B7S5vXRUqzbpxJciSGFZCCWwRei8laoSqmCreAhYgXWva680ftzeZB89S9gbqZBCdPm5Tf0jcxxFQZDZD'
VERIFY_TOKEN = 'TESTINGTOKEN'
bot = Bot(ACCESS_TOKEN)

contestFile = 'contest.json'
# broker_url = 'pyamqp://guest@localhost//'  for localhost 
broker_url1 = 'amqp://etpgqwsn:K9K3QCwBkCOmgHEPYDdcnpjoJKO_4ThI@eagle.rmq.cloudamqp.com/etpgqwsn'
app = Celery('celery_tasks' ,broker=broker_url1)

def readFromFile():
    with open(contestFile) as json_file:
        return json.load(json_file)

def searchInJSON(platform,startTime,endTime):  
    contests = readFromFile()
    tempContests = []
    for contest in contests:
        if contest in platform:
            tempContests.append(contest)

def send_message_from_messenger(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def send_message_from_zulip(recipient_id, response):
    req = {
            "type": "private",
            "to": recipient_id,
            "content": response
        }
    client.send_message(req)

@app.task
def reminder(konsa, reply, user):
    if konsa == "messenger":    
        send_message_from_messenger(user, reply)
    elif konsa == "zulip":
        send_message_from_zulip(user, reply)





    
    