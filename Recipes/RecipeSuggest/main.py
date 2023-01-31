# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup


url = 'http://www.bbc.com/news'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
top_stories = soup.find_all('a', class_='gs-c-promo-heading')
for story in top_stories:
    print(story.text)

