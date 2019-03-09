from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 
from dateutil.parser import parse

def hackerearth():
    options = Options()
    options.add_argument("--headless")
    chromedriverPath = '../chrome/chromedriver'
    browser = webdriver.Chrome(executable_path=chromedriverPath,chrome_options=options)
    browser.get('https://www.hackerearth.com/challenges/')
    loop_var =0
    contest_array = []
    while loop_var<10:
        loop_var+=1
        try:
            tempData = browser.find_element_by_class_name("upcoming")
            contests = tempData.find_elements_by_class_name("challenge-card-modern")
            for contest in contests:
                tempContest = contest.find_element_by_tag_name('a')
                contestLink = tempContest.get_attribute('href')
                tempContest = tempContest.find_element_by_class_name('challenge-content')
                contestData = tempContest.find_elements_by_tag_name('div')
                contestType = contestData[0].text
                contestName = contestData[1].text
                contestTime = contestData[2].find_element_by_class_name('date').text
                contestTime = parse(contestTime)
                tempJSON = {
                    'contestLink': contestLink,
                    'contestType': contestType,
                    'contestName': contestName,
                    'contestTime': contestTime
                }
                contest_array.append(tempJSON)
            print("Done")
            break
        except Exception as E:
            print(E)
            print("Error!!\n")
            sleep(5)
    browser.close()
    return contest_array

arr = hackerearth()
print(arr)