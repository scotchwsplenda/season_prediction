
# https://pbpython.com/pandas-html-table.html
import pandas as pd
import sqlite3
import numpy as np

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

# https://stackoverflow.com/questions/39109045/numpy-where-with-multiple-conditions -> answer #2
#  sqlite3.connect must have '../' before db file in order to navigate up one directory
def accurate_wl():
    # table for pred spread
    df_predictions = pd.read_sql('SELECT * FROM vPredicted_Score_Dif', sqlite3.connect('../db.sqlite3'))
    funky = get_df_panda()
    # table for difference between predicted and actual spread
    df_accurate_wl = pd.DataFrame()
    df_accurate_wl['Name'] = df_predictions['username']
    df_accurate_wl['WEEK1'] = np.where(
        ((df_predictions['Pred_Wk1_Spred'] * funky['Differenchy'][0]) > 0), # correctly predicted W/L 
         (df_predictions['Pred_Wk1_Spred'] - funky['Differenchy'][0]).abs(),None) # dif between actual and predicted, (if W/L wrong -1)
    df_accurate_wl['WEEK2'] = np.where(
        ((df_predictions['Pred_Wk2_Spred'] * funky['Differenchy'][1]) > 0), 
         (df_predictions['Pred_Wk2_Spred'] - funky['Differenchy'][1]).abs(),None) 
    df_accurate_wl['WEEK3'] = np.where(
        ((df_predictions['Pred_Wk3_Spred'] * funky['Differenchy'][2]) > 0), 
         (df_predictions['Pred_Wk3_Spred'] - funky['Differenchy'][2]).abs(),None) 
    df_accurate_wl['WEEK4'] = np.where(
        ((df_predictions['Pred_Wk4_Spred'] * funky['Differenchy'][3]) > 0),
         (df_predictions['Pred_Wk4_Spred'] - funky['Differenchy'][3]).abs(),None) 
    df_accurate_wl['WEEK5'] = np.where(
        ((df_predictions['Pred_Wk5_Spred'] * funky['Differenchy'][4]) > 0), 
         (df_predictions['Pred_Wk5_Spred'] - funky['Differenchy'][4]).abs(),None) 
    df_accurate_wl['WEEK6'] = np.where(
        ((df_predictions['Pred_Wk6_Spred'] * funky['Differenchy'][5]) > 0), 
         (df_predictions['Pred_Wk6_Spred'] - funky['Differenchy'][5]).abs(),None) 
    df_accurate_wl['WEEK7'] = np.where(
        ((df_predictions['Pred_Wk7_Spred'] * funky['Differenchy'][6]) > 0), 
         (df_predictions['Pred_Wk7_Spred'] - funky['Differenchy'][6]).abs(),None) 
    df_accurate_wl['WEEK8'] = np.where(
        ((df_predictions['Pred_Wk8_Spred'] * funky['Differenchy'][7]) > 0),
         (df_predictions['Pred_Wk8_Spred'] - funky['Differenchy'][7]).abs(),None) 
    df_accurate_wl['WEEK9'] = np.where(
        ((df_predictions['Pred_Wk9_Spred'] * funky['Differenchy'][8]) > 0), 
         (df_predictions['Pred_Wk9_Spred'] - funky['Differenchy'][8]).abs(),None) 
    df_accurate_wl['WEEK10'] = np.where(
        ((df_predictions['Pred_Wk10_Spred'] * funky['Differenchy'][9]) > 0), 
         (df_predictions['Pred_Wk10_Spred'] - funky['Differenchy'][9]).abs(),None) 
    df_accurate_wl['WEEK11'] = np.where(
        ((df_predictions['Pred_Wk11_Spred'] * funky['Differenchy'][10]) > 0), 
         (df_predictions['Pred_Wk11_Spred'] - funky['Differenchy'][10]).abs(),None) 
    df_accurate_wl['WEEK12'] = np.where(
        ((df_predictions['Pred_Wk12_Spred'] * funky['Differenchy'][11]) > 0),
         (df_predictions['Pred_Wk12_Spred'] - funky['Differenchy'][11]).abs(),None) 
    df_accurate_wl['WEEK13'] = np.where(
        ((df_predictions['Pred_Wk13_Spred'] * funky['Differenchy'][12]) > 0), 
         (df_predictions['Pred_Wk13_Spred'] - funky['Differenchy'][12]).abs(),None) 
    df_accurate_wl['WEEK14'] = np.where(
        ((df_predictions['Pred_Wk14_Spred'] * funky['Differenchy'][13]) > 0), 
         (df_predictions['Pred_Wk14_Spred'] - funky['Differenchy'][13]).abs(),None) 
    df_accurate_wl['WEEK15'] = np.where(
        ((df_predictions['Pred_Wk15_Spred'] * funky['Differenchy'][14]) > 0), 
         (df_predictions['Pred_Wk15_Spred'] - funky['Differenchy'][14]).abs(),None) 
    df_accurate_wl['WEEK16'] = np.where(
        ((df_predictions['Pred_Wk16_Spred'] * funky['Differenchy'][15]) > 0),
         (df_predictions['Pred_Wk16_Spred'] - funky['Differenchy'][15]).abs(),None) 
    df_accurate_wl['WEEK17'] = np.where(
        ((df_predictions['Pred_Wk17_Spred'] * funky['Differenchy'][16]) > 0), 
         (df_predictions['Pred_Wk17_Spred'] - funky['Differenchy'][16]).abs(),None)
    cut_conditions = [0,3.5,7.5,10.5,100]
    cut_scores = [1,.95,.9,.85]
    df_accurate_wl_funk = df_accurate_wl.fillna(-1)
    df_predictions_accuracy = pd.DataFrame()
    df_predictions_accuracy['name'] = df_accurate_wl.iloc[:,0]
    df_predictions_accuracy['WEEK1'] = pd.cut(df_accurate_wl_funk['WEEK1'],bins = cut_conditions, labels = cut_scores)
    return df_predictions_accuracy


print(accurate_wl())