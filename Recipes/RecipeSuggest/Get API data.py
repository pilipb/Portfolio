import pandas as pandas
import requests as requests
import json
# install requests
# pandas
# import mysql.connector
# from mysql.connector import Error
import pandas as pd
import requests
import pandas as pd

url = "https://tasty.p.rapidapi.com/recipes/list"
numberResponses = 10
tags = ['under_30_minutes', 'vegetarian']
ingredients = ['rice']

querystring = {"prefix":None,"from": "0", "size": numberResponses, "tags": None}

headers = {
    'x-rapidapi-host': "tasty.p.rapidapi.com",
    'x-rapidapi-key': "2802f6d8ddmsh23590b8e00782edp1e2548jsna6f6a4ae3eea"
}

response = requests.request("GET", url, headers=headers, params=querystring)
# temp_df = pd.DataFrame(response.json()["results"])[['id','title','overview','popularity','release_date','vote_average','vote_count']]
results_df = response.json()
# ['results']['name','user_ratings','total_time_minutes','tags',
#                                                        'nutrition','total_time_tier','yields',
#                                                        'keywords','num_servings','sections',
#                                                        'instructions']
print(results_df)
# results_df.describe()
# print(response.json())

# sortResults = results_df.sort_values('keywords',axis=0,ascending=True)

# print(sortResults)
