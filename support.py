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
    
    print(inp)
        

    output = do_what_i_say(inp)
    print(output)


    res = {
        "fulfillmentText": "fulfillmentText",
        "fulfillmentMessages":
        [
            {
                "simpleResponses":
                {
                    "simpleResponses":
                    [
                        {
                            "textToSpeech":"textToSpeech",
                            "displayText":"displayText"
                        }
                    ]
                }
            }
        ],
        "source":"webhook-sample"
    }
    for contest in output:
        contest['startTime'] = str(contest['startTime'])
        contest['endTime'] = str(contest['endTime'])
    output = json.dumps(output,indent=4)
    resp = Response(output)
    resp.headers['Content-Type'] = 'application/json'

    return resp


if __name__ == '__main__':
    p1 = Process(target=process.ini)
    p1.start()
    
    app.run(debug=True, host='0.0.0.0')

p1.join()