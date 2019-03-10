def get_response(msg):
    # print("yo")
    msg = msg.lower()

    if 'reminder' in msg:
        l = []
        num = 0
        for i in range(len(msg)):
            if msg[i] >= '0' and msg[i]<='9':
                num = num*10+(int(msg[i]))
            else:
                if num:
                    l.append(num)
                num=0
        if num:
            l.append(num)
        
        return l

    if 'hi' in msg or 'hello' in msg:
        out = 'Hello ! I am ContestBot'
        return [out]

    elif 'bye' in msg or 'tata' in msg:
        out = 'Goodbye ! See you soon!'
        return [out]
    
    # elif 'show' in msg and 'contests' in msg:
    #     out = 'Select Platforms:\n'+ str(1) + ' Codeforces\n' + str(2) + ' Codechef\n' + str(3) + ' HackerEarth'
    #     return [out]
    
    out = [{ 'platform': [] }]

    if 'codeforces' in msg or 'cf' in msg or 'all' in msg:
        out[0]['platform'].append('codeforces')
    
    if 'hackerearth' in msg or 'he' in msg or 'all' in msg:
        out[0]['platform'].append('hackerearth')

    if 'codechef' in msg or 'cc' in msg or 'all' in msg:
        out[0]['platform'].append('codechef')

    return out 



# get_response("set reminder for 2,3,25")

