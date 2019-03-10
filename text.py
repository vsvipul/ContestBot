
def get_response(msg):

    msg = msg.lower()

    # if 'reminder' in msg:

    if 'hi' in msg or 'hello' in msg:
        out = 'Hello ! I am ContestBot'
        return [out]
    
    elif 'show' in msg and 'contests' in msg:
        out = 'Select Platforms:\n'+ str(1) + ' Codeforces\n' + str(2) + ' Codechef\n' + str(3) + ' HackerEarth'
        return [out]
    
    out = [{ 'platform': [] }]

    if 'codeforces' in msg or 'cf' in msg:
        out[0]['platform'].append('codeforces')
    
    if 'hackerearth' in msg or 'he' in msg:
        out[0]['platform'].append('hackerearth')

    if 'codechef' in msg or 'cc' in msg:
        out[0]['platform'].append('codechef')

    return out 



    

