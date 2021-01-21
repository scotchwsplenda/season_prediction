
# https://pbpython.com/pandas-html-table.html
import pandas as pd
import sqlite3



def get_df_panda():
    url = 'https://www.pro-football-reference.com/teams/sea/2020.htm'
    table = pd.read_html(url, match='Game Results Table')
    df = table[0]
    # declare exach column to deal with 'multiindexing, then select the ones you want
    df.columns=['Week','Day','Date','Time','BoxScore','Result','OT','Rec','Home_Away','Opp','HawkScore','OppScore','1stD','TotYd','PassY','RushY','TO','1stD','TotYd','PassY','RushY','TO','Offense','Defense','Sp. Tms']
    funky = df[['Week','Day','Date','Time','Result','OT','Rec','Home_Away','Opp','HawkScore','OppScore']].reset_index(drop=True)
    funky.loc[df['Day'].isnull(), 'Day'] = 'Bye'
    funky.loc[df['Home_Away'].isnull(), 'Home_Away'] = 'VS.'
    funky.loc[df['Home_Away'] == '@', 'Home_Away'] = 'AT'
    funky['Differenchy'] = funky["HawkScore"] -funky['OppScore'] 
    funky['Title'] = 'WEEK ' + funky['Week'].map(str) + ': ' + funky['Home_Away'].map(str) +' ' + funky["Opp"].map(str)
    funky = funky.reset_index(drop=True).set_index('Week')
    return funky

def seahawks_season_to_sql(funky):
    conn = sqlite3.connect('db.sqlite3')
    print(funky)
    funky.to_sql('gohawks_hawksseason', conn, if_exists='replace')
    
def seahawks_season_transposed_to_sql(funky):
    oppscore = funky.T
    tops = oppscore.reset_index()
    rocks = tops.loc[7:11,:]
    print(rocks)
    conn = sqlite3.connect('db.sqlite3')
    rocks.to_sql('gohawks_seahawksseasontransposed', conn, if_exists='replace')

if __name__ == '__main__':
    seahawks_season_to_sql(get_df_panda())
    seahawks_season_transposed_to_sql(get_df_panda())



'''  
y1960 = pd.read_sql('SELECT * FROM seahawks_season', sqlite3.connect('db.sqlite3'))
print(y1960)
y1961 = pd.read_sql('SELECT * FROM seahawks_season_transposed', sqlite3.connect('db.sqlite3'))
print(y1961)
'''

'''
CLEAN with 'case when'
    https://datatofish.com/if-condition-in-pandas-dataframe/
    # can't change NaN values to 'int'
TURN INTO A SQL TABLE
    https://towardsdatascience.com/python-pandas-and-sqlite-a0e2c052456f
    https://datatofish.com/pandas-dataframe-to-sql/
CREATE MODEL FROM SQL TABLE
    python manage.py inspectdb > models.py
CREAT FORM FROM MODEL
    https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
'''
