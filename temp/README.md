## ContestBot
A contest bot created during Hack On Hills 2019 at NIT Hamirpur. 

## Problem Solution
This bot aims to make the life of competitive programmers easy. This bot helps in reminding programmers about programming contests held on various platforms like codechef, hackerearth and codeforces and the users can also command the bot to set reminders about any contest they wish to participate in.

## Technologies Used

- Python
- DialogFlow (NLP)
- BeautifulSoup and Selenium (for webscraping)
- Celery (for  asynchronous task queue/job queue)
- Zulip API
- FB Messenger API

### How to run

1.  Clone this repo.  


## What can it do?
ContestBot can do a variety of things related to online competitive programming contests and make the life of coders easy. Some of them are-
- Lookup contests on various websites and provide it to the user.
- Show time remaining for all the contests, listed platform-wise.
- Users can set reminders for any contest they wish to participate in.  

## How does it work?
- ContestBot runs a web-scraping job (scrapper.py) every 6 hours, to fetch contest related details from platforms like Codechef, Hackerearth and Codeforces and then stores it in the backend. This is done using Selenium (for dynamic pages like Codeforces) and BeautifulSoup (for static pages like Codechef).
- The main process (process.py) runs on the server and listens to responses from Zulip/ FB Messenger, then DialogFlow processes the message to get the relevant response, which contains the contest info from the backend. 

## How to contribute?
Clone the repo and feel free to send any Pull Requests that you feel to be contructive.
