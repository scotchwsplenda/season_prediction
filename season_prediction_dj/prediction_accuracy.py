
# https://pbpython.com/pandas-html-table.html
import pandas as pd
import sqlite3
import numpy as np
from pandas.core.frame import DataFrame
# from season_prediction_dj.seahawks_2022_predictions.models import prediction_table
from django_pandas.io import read_frame

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
    funky['Differenchy'] =  funky['Differenchy'].fillna(-99)
    # funky['Differenchy'].astype(int)
    funky['Title'] = 'WEEK ' + funky['Week'].map(str) + ': ' + funky['Home_Away'].map(str) +' ' + funky["Opp"].map(str)
    funky = funky.reset_index(drop=True).set_index('Week')
    return funky

def predictions_accuracy(funky):
    df_predictions = pd.read_sql('SELECT id, name, Predicted_HawkScore_Wk1 -  Predicted_OppScore_Wk1 as Predicted_Wk1_Score_Dif, Predicted_HawkScore_Wk2 -  Predicted_OppScore_Wk2 as Predicted_Wk2_Score_Dif, Predicted_HawkScore_Wk3 -  Predicted_OppScore_Wk3 as Predicted_Wk3_Score_Dif, Predicted_HawkScore_Wk4 -  Predicted_OppScore_Wk4 as Predicted_Wk4_Score_Dif, Predicted_HawkScore_Wk5 -  Predicted_OppScore_Wk5 as Predicted_Wk5_Score_Dif, Predicted_HawkScore_Wk6 -  Predicted_OppScore_Wk6 as Predicted_Wk6_Score_Dif, Predicted_HawkScore_Wk7 -  Predicted_OppScore_Wk7 as Predicted_Wk7_Score_Dif, Predicted_HawkScore_Wk8 -  Predicted_OppScore_Wk8 as Predicted_Wk8_Score_Dif, Predicted_HawkScore_Wk9 -  Predicted_OppScore_Wk9 as Predicted_Wk9_Score_Dif, Predicted_HawkScore_Wk10 - Predicted_OppScore_Wk10 as Predicted_Wk10_Score_Dif, Predicted_HawkScore_Wk11 - Predicted_OppScore_Wk11 as Predicted_Wk11_Score_Dif, Predicted_HawkScore_Wk12 - Predicted_OppScore_Wk12 as Predicted_Wk12_Score_Dif, Predicted_HawkScore_Wk13 - Predicted_OppScore_Wk13 as Predicted_Wk13_Score_Dif, Predicted_HawkScore_Wk14 - Predicted_OppScore_Wk14 as Predicted_Wk14_Score_Dif, Predicted_HawkScore_Wk15 - Predicted_OppScore_Wk15 as Predicted_Wk15_Score_Dif, Predicted_HawkScore_Wk16 - Predicted_OppScore_Wk16 as Predicted_Wk16_Score_Dif, Predicted_HawkScore_Wk17 - Predicted_OppScore_Wk17 as Predicted_Wk17_Score_Dif FROM seahawks_2022_predictions_prediction_table;', sqlite3.connect('db.sqlite3'))
    funky.astype({'Differenchy': 'int64'})
    df_accuracy = pd.DataFrame(columns=['Name','WEEK1','WEEK2','WEEK3'])
    df_accuracy['Name'] = df_predictions['name']
    df_accuracy['WEEK1'] = (df_predictions['Predicted_Wk1_Score_Dif']- funky['Differenchy'][0])
    print(df_accuracy)
    print(funky['Differenchy'])
    print(df_predictions['Predicted_Wk1_Score_Dif'])

predictions_accuracy(get_df_panda())
