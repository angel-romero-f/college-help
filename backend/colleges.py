# this file is for fetching data from the api import requests
import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint

# Base URL
URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

# function that makes a call to the api and passess in neccesary parameters
def get_college_info(college_name):
    global URL

    # I used a placeholder parameter for now, but we append the ones that are passed in as input into the "params" dictionary
    params = {
    'api_key':"9cx6Llu0TXhNipn0XjML7TTictmFY8eKAJtmn2aQ",
    'school.name': college_name,
    'fields': 'latest.school.name,latest.school.city,latest.school.state,latest.student.size,latest.cost.tuition.in_state'
    }

    list_of_schools = requests.get(URL, params=params).json()['results']
    return pd.DataFrame(list_of_schools).fillna('N/A')


# def save_to_json(data, filename):
#     with open(filename, 'w') as json_file:
#         json.dump(data, json_file, indent=4)

# ret = get_college_info("harvard").json()

# save_to_json(ret, 'college_info.json')
        
# df = pd.json_normalize(ret['results'])

# df = df[['latest.school.name', 'latest.school.city', 'latest.school.state', 'latest.student.size', 'latest.cost.tuition.in_state']]

# engine = db.create_engine('sqlite:///locations.db')

# df.to_sql('colleges', con=engine, if_exists='append', index=False)

# df.rename(columns={'latest.school.name':'Name', 'latest.school.city':'City', 'latest.school.state':'State', 'latest.student.size':'Size', 'latest.cost.tuition.in_state':'Tuition'}, inplace=True)

# query_result = ""
# with engine.connect() as connection:
#     query_result = connection.execute(db.text("SELECT * FROM colleges WHERE Name = college_name;")).fetchall()
#     print(pd.DataFrame(query_result))
    
# result = [dict(row) for row in query_result]

# print(result)


