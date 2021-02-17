
# https://pbpython.com/pandas-html-table.html
import pandas as pd
import sqlite3
import numpy as np
from hawksscore import get_df_panda


dd = get_df_panda().reset_index(drop = True)
dd = dd.loc[:16,['Title','Differenchy']]
df_predictions = pd.read_sql('SELECT * FROM vPredicted_Score_Dif', sqlite3.connect('../db.sqlite3'))
df_predictions = df_predictions.T
new_header = df_predictions.iloc[0] #grab the first row for the header
df_predictions = df_predictions[1:] #take the data less the header row
df_predictions.columns = new_header #set the header row as the df header
df_predictions = df_predictions.reset_index(drop = True)
bigdata = pd.merge(dd, df_predictions, left_index=True, right_index=True)
bigdata = bigdata.fillna(0)
bigdata['Differenchy'] = bigdata['Differenchy'].astype(int)
# print(bigdata)


# print(np.subtract(bigdata['Differenchy'], bigdata['Ken']))
# https://stackoverflow.com/questions/26333005/numpy-subtract-every-row-of-matrix-by-vector/26333184
v = bigdata['Differenchy'][:, np.newaxis]
# print(type(v))

# for x in v:
#     print(type(x))

# print(bigdata.iloc[:,1:])
# print(bigdata.iloc[:,1:]-v)
c = bigdata['Differenchy']
for x in c:
    print(x)
# print(type(c))

dumn = []
for index, row in bigdata.iterrows():
    dumn.append(np.where((row[1] * row[2:]) > 0, (row[1] - row[2:]).abs(), None))
print(dumn)


    # print(type(index))
    # print(index)
    # print('~~~~~~')

    # print(type(row))
    # print(row)
    # print('------')


    # print(np.where((column * v) > 0, (column - v).abs(), None))

'''
df_accurate_wl['WEEK1'] = np.where(
    ((df_predictions['Pred_Wk1_Spred'] * funky['Differenchy'][0]) > 0), # correctly predicted W/L 
        (df_predictions['Pred_Wk1_Spred'] - funky['Differenchy'][0]).abs(),None) # dif between actual and predicted, (if W/L wrong -1)
'''