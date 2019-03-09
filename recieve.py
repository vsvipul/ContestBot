import zulip
client = zulip.Client(config_file="zuliprc")
i =0
while 1:
    i+=1
    request = {
        'use_first_unread_anchor':True,
        'num_before': 0,
        'num_after': 0,
        'narrow': [{
            'operator': 'is',
            'operand': 'private'
        }]
    }
    result = client.get_messages(request)
    messages = result['messages']
    for message in messages:
        id = message['id']
        text = message['content']
        reply_to = message['sender_email']
        print(str(id)+" "+text)
        req = {
            'messages' : [id],
            'op': 'add',
            'flag': 'read'
        }
        result = client.update_message_flags(req)
        print(result)
        print(text+'\n')
        req = {
            "type": "private",
            "to": reply_to,
            "content": "Go To Hell!!!"
        }
        result = client.send_message(req)
        read_id = result['id']
        print(read_id)
        try:
            req = {
                'messages' : [read_id],
                'op': 'add',
                'flag': 'read'
            }
            result = client.update_message_flags(req)
        except:
            print("Error!")
        print(result)
        
