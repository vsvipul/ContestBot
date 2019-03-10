import zulip
import process
from multiprocessing import Process
from queue import Queue
from time import sleep
client = zulip.Client(config_file="zuliprc")
i =0
queue = Queue()
def runzulip():
    while 1:
        requestPriv = {
            'use_first_unread_anchor':True,
            'num_before': 0,
            'num_after': 0,
            'narrow': [{
                'operator': 'is',
                'operand': 'private'
            }
            ],
            'apply_markdown': True
        }
        requestMent = {
            'use_first_unread_anchor':True,
            'num_before': 0,
            'num_after': 0,
            'narrow': [{
                'operator': 'is',
                'operand': 'mentioned'
            }
            ],
            'apply_markdown': True
        }
        sleep(1)
        try:
            resultpriv = client.get_messages(requestPriv)
            resultment = client.get_messages(requestMent)
            messages = resultpriv['messages']+resultment['messages']
            for message in messages:
                id = message['id']
                text = message['content']
                reply_to = message['sender_email']
                reply = process.get_message(text,reply_to,'zulip')

                queue.put({'text':reply,'reply':reply_to})
                print(str(id)+" "+text)
                req = {
                    'messages' : [id],
                    'op': 'add',
                    'flag': 'read'
                }
                result = client.update_message_flags(req)
                print(result)
                print(text+'\n')
                for rep in reply:
                    req = {
                        "type": "private",
                        "to": reply_to,
                        "content": rep
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
        except:
            sleep(1)
if __name__ == "__main__":
    p = Process(target=runzulip)
    p.start()
    p.join()
