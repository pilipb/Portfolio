# function to scrape top ten news stories from bbc.com

import requests
from bs4 import BeautifulSoup


url = 'http://www.bbc.com/news'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
top_stories = soup.find_all('a', class_='gs-c-promo-heading')
for story in top_stories:
    print(story.text)




