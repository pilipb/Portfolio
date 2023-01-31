import requests
import pandas as pd
import json

# rm_main is a mandatory function,
# the number of arguments has to be the number of input ports (can be none)
def rm_main():
    username = YOUR USERNAME GOES HERE
    password = YOUR PASSWORD GOES HERE

    s = requests.Session()
    link = URL GOES HERE

    response = s.get(link, auth = (username, password), verify = False)
    data = json.loads((response.content).decode('utf-8'))
    temp = []
    ratings = data['ratings']
    for i in ratings:
        rating_date = i['rating_date']
        rating = i['rating']
        range_nm = i['range']
        rating_color = i['rating_color']
        temp.append([rating_date, rating, range_nm, rating_color])

df = pd.DataFrame(temp,columns = ['rating_dt','rating', 'range_nm', 'rating_color'])
