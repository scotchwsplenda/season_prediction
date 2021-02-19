
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


# https://stackoverflow.com/questions/26333005/numpy-subtract-every-row-of-matrix-by-vector/26333184
v = bigdata['Differenchy'][:, np.newaxis]

dumb=[]
for index, row in bigdata.iterrows():
    zz = np.where((row[1] * row[2:]) > 0, (row[1] - row[2:]).abs(), None).tolist()
    zz.insert(0,row[1])
    zz.insert(0,row[0])
    dumb.append(zz)
    print(zz)
dumb = np.array(dumb)
df = pd.DataFrame(dumb, columns=bigdata.columns.to_list())

# def condformat(row):
#     color = 'background-color: {}'.format('green' if row.value >0 else 'red')
#     return (color, color)

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'green'
    return 'color: %s' % color

s = df.style.apply(color_negative_red, axis=0)


print(s)

