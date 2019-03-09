import json
from process import do_what_i_say
import process
from flask import Flask, request, make_response, jsonify,Response
from multiprocessing import Process
app = Flask(__name__)
log = app.logger


@app.route('/page', methods=['GET','POST'])
def webhook():

    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    inp = []

    if action == 'platform':
        # print(req['queryResult']['parameters'])
        if len(req['queryResult']['parameters']) == 0:
            inp.append(['Codeforces','Codechef','Hackerearth'])
        else:
            inp.append(req['queryResult']['parameters'])

        inp.append("search")

    elif action == 'reminder': # make necessary arrangements for index of reminder,also configure in diagflow
        inp.append(None)
        inp.append("reminder")

    
    # print(inp)
        
    output = do_what_i_say(inp)
    # print(output)

    res = {
        "fulfillmentText": "fulfillmentText",
        "fulfillmentMessages":[],
        "source":"contests from webhook"
    }
    
    for contest in output:
        displayText = contest['name'] + " From: "+str(contest['startTime']) + " To: "+str(contest['endTime']) + " on "+contest['platform']+ ". Go to: "+contest['link']

        temp = {'simpleResponses':{'simpleResponses':[{"speech": "Text response",'displayText':displayText}]}}
        res['fulfillmentMessages'].append(temp)

    # Display this text in zulip and messenger

    
    output = json.dumps(res,indent=4)
    resp = Response(output)
    resp.headers['Content-Type'] = 'application/json'

    return resp


if __name__ == '__main__':
    p1 = Process(target=process.ini)
    p1.start()
    
    app.run(debug=True, host='0.0.0.0')

p1.join()