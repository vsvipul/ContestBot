
def get_response(msg):

    msg = msg.lower()

    # if 'reminder' in msg:

    if msg == 'hi' or msg == 'hello':
        out = 'Hello ! I am ContestBot'
        return out
    
    elif 'show' in msg and 'contests' in msg:
        out = 'Select Platforms:\n'+ str(1) + ' Codeforces\n' + str(2) + ' Codechef\n' + str(3) + ' HackerEarth'
        return out
    
    out = [{ 'platform': [] }]

    if 'codeforces' in msg :
        out['platform'].append('codeforces')
    
    if 'hackerearth' in msg:
        out['platform'].append('hackerearth')

    if 'codechef' in msg :
        out['platform'].append('codechef')

    return out 



    

