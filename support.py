import json

from flask import Flask, request, make_response, jsonify,Response

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
        inp.append(req['queryResult']['parameters'])
    
        

    output = fuckyeah(inp)



    # res = {
    #     "fulfillmentText": "fulfillmentText",
    #     "fulfillmentMessages":
    #     [
    #         {
    #             "simpleResponses":
    #             {
    #                 "simpleResponses":
    #                 [
    #                     {
    #                         "textToSpeech":"textToSpeech",
    #                         "displayText":"displayText"
    #                     }
    #                 ]
    #             }
    #         }
    #     ],
    #     "source":"webhook-sample"
    # }

    output = json.dumps(output,indent=4)
    resp = Response(output)
    resp.headers['Content-Type'] = 'application/json'

    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')