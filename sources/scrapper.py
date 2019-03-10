import sources.codechef as codechef
import sources.hackerearth as hackerearth
import sources.codeforces as codeforces

def process():
    # Scrapping Codeforces
    contests = []
    tempContests = codeforces.codeforces()
    contests = contests+ tempContests
    #Scraping Codechef
    tempContests = codechef.codechef()
    contests = contests+ tempContests
    #Scraping Hackerearth
    tempContests = hackerearth.hackerearth()
    contests = contests+ tempContests
    return contests
