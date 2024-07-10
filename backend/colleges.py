# this file is for fetching data from the api import requests
import requests
import json
import sqlalchemy as db
import pandas as pd
import pprint

# Base URL
URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

# function that makes a call to the api and passess in neccesary parameters
def get_college_info(WE_CAN_PASS_IN_PARAMS_HERE):
    global URL

    # I used a placeholder parameter for now, but we append the ones that are passed in as input into the "params" dictionary
    params = {
    'api_key':"9cx6Llu0TXhNipn0XjML7TTictmFY8eKAJtmn2aQ",
    'school.name':'Harvard University',
    }

    return requests.get(URL, params=params)

#print(json.dumps(get_college_info("f").json(), indent=3))

######################
## FILTER DATA HERE 
##
##
######################

#convert resulting dictionary to pandas dataframe
# this df will be used in the main.py file
# the "f" is a placeholder for now
ret = dict(get_college_info("f").json())

# initialize data of lists.
nams = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
ret = pd.DataFrame(nams)
college_info_db = pd.DataFrame.from_dict(ret)
#print(college_info_db)






#### note: I found everything below this point to be extra, so I did not include it ####

## convert dataframe to sql, and create a file with with the data with a .db extension ##
#engine = db.create_engine('sqlite:///college_info.db')
#college_info_db.to_sql('college', con=engine, if_exists='replace', index=False)

#with engine.connect() as connection:
#   query_result = connection.execute(db.text("SELECT * FROM college;")).fetchall()
