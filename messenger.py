import random
from flask import Flask, request
from pymessenger.bot import Bot
# import sources.hackerearth as hackerearth
import process as process


app = Flask(__name__)
ACCESS_TOKEN = 'EAALxONaYePsBAM5oBExC3ZC9yFGVucIiZB7fxP00AKhZBc9gjPZAqtk7Ed8T8UlD8bhZBsA8pWIcSpPrGpItvUSEk1ZAMPfZBr6B7S5vXRUqzbpxJciSGFZCCWwRei8laoSqmCreAhYgXWva680ftzeZB89S9gbqZBCdPm5Tf0jcxxFQZDZD'
VERIFY_TOKEN = 'TESTINGTOKEN'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                print(recipient_id)
                if message['message'].get('text'):
                    msg = message['message'].get('text')
                    response_sent_text = process.get_message(msg , recipient_id , 'fb')
                    send_message(recipient_id, response_sent_text)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()