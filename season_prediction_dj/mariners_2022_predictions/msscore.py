
# https://pbpython.com/pandas-html-table.html
import pandas as pd
import sqlite3
import numpy as np
from pandas.core.frame import DataFrame
# from .models import prediction_table
from django_pandas.io import read_frame

# .season_prediction_dj.seahawks_2022_predictions
url = 'https://www.cbssports.com/mlb/teams/SEA/seattle-mariners/schedule/regular/'
table = pd.read_html(url)
print(type(table))
# print(table[0])
table = table[0] # for some fucking reason you have to say its the first thing ([0])
print(table.columns)
table = table.iloc[:,:5]

table['Date'] = table['Date'].replace([', 2021'], '', regex=True) # the regex is what makes it read only part of the string
# print(table['OPP'].str[:2])
table['WHERE'] = np.where(table['OPP'].str[:2]=='vs',"HOME",'AWAY')
table["OPP"] = table["OPP"].str.split(" ",1).str[1]
# https://datatofish.com/left-right-mid-pandas/
print(table[:9])

# group and order by size
dumb  = table.groupby(['OPP']).size()
print(dumb.sort_values(ascending=False))


# def get_df_panda():
#     url = 'https://www.cbssports.com/mlb/teams/SEA/seattle-mariners/schedule/regular/'
#     table = pd.read_html(url, match='Game Results Table')
#     df = table[0]
#     # declare exach column to deal with 'multiindexing, then select the ones you want
#     df.columns=['Week','Day','Date','Time','BoxScore','Result','OT','Rec','Home_Away','Opp','HawkScore','OppScore','1stD','TotYd','PassY','RushY','TO','1stD','TotYd','PassY','RushY','TO','Offense','Defense','Sp. Tms']
#     funky = df[['Week','Day','Date','Time','Result','OT','Rec','Home_Away','Opp','HawkScore','OppScore']].reset_index(drop=True)
#     funky.loc[df['Day'].isnull(), 'Day'] = 'Bye'
#     funky.loc[df['Home_Away'].isnull(), 'Home_Away'] = 'VS.'
#     funky.loc[df['Home_Away'] == '@', 'Home_Away'] = 'AT'
#     funky['Differenchy'] = funky["HawkScore"] -funky['OppScore'] 
#     funky['Title'] = 'WEEK ' + funky['Week'].map(str) + ': ' + funky['Home_Away'].map(str) +' ' + funky["Opp"].map(str)
#     funky = funky.reset_index(drop=True).set_index('Week')
#     return funky

# def seahawks_season_to_sql(funky):
#     conn = sqlite3.connect('db.sqlite3')
#     print(funky)
#     funky.to_sql('gohawks_hawksseason', conn, if_exists='replace')
    
# def seahawks_season_transposed_to_sql(funky):
#     oppscore = funky.T
#     tops = oppscore.reset_index()
#     rocks = tops.loc[7:11,:]
#     print(rocks)
#     conn = sqlite3.connect('db.sqlite3')
#     rocks.to_sql('gohawks_seahawksseasontransposed', conn, if_exists='replace')
