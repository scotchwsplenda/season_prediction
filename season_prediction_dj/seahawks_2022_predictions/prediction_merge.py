
# https://pbpython.com/pandas-html-table.html
import pandas as pd
import sqlite3
import numpy as np
from hawksscore import get_df_panda


# loc is by name iloc is by idex
oppscore = get_df_panda().T

dd = get_df_panda().reset_index(drop = True)
dd = dd.loc[:16,['Title','Differenchy']]



df_predictions = pd.read_sql('SELECT * FROM vPredicted_Score_Dif', sqlite3.connect('../db.sqlite3'))
df_predictions = df_predictions.T
# make columns equal
new_header = df_predictions.iloc[0] #grab the first row for the header
df_predictions = df_predictions[1:] #take the data less the header row
df_predictions.columns = new_header #set the header row as the df header
df_predictions = df_predictions.reset_index(drop = True)
print(df_predictions.shape)
print(dd.shape)
print(df_predictions)
print(dd)

# bigdata = pd.concat([dd, df_predictions], axis=0, ignore_index=True)
# print(bigdata)

bigdata = pd.merge(dd, df_predictions, left_index=True, right_index=True)
print(bigdata)

# bigdata = dd.insert(df_predictions,)
# print(bigdata)