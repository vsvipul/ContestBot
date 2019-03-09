import sources.codechef as codechef
import sources.hackerearth as hackerearth
import sources.codeforces as codeforces

def process():
    # Scrapping Codeforces
    contests = []
    tempContests = codeforces.codeforces()
    contests.append(tempContests)
    #Scraping Codechef
    tempContests = codechef.codechef()
    contests.append(tempContests)
    #Scraping Hackerearth
    tempContests = hackerearth.hackerearth()
    contests.append(tempContests)
    return contests

if __name__ == "__main__":
    process()