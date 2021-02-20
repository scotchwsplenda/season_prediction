from django.shortcuts import render, redirect
from .forms import prediction_form
from .hawksscore import get_df_panda
from datetime import datetime

import pandas as pd
import sqlite3
import numpy as np
# Create your views here.

def hawks_predictions_form(request):
    season2 = get_df_panda()
    if request.method == "POST":
        form = prediction_form(request.POST, initial = {'Submitted_Date': datetime.now()})
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.Submitted_Date = datetime.now()
            print(request.POST)
            instance.save()
            return redirect('/')
    else:
        form = prediction_form()
    return render(request, "seahawks_2022_predictions/form.html", {'form': form, 'season': season2})

def hawks_scores_view(request):
    return render(request, "seahawks_2022_predictions/home.html", {'get_df_panda': get_df_panda().to_html()})


# https://stackoverflow.com/questions/39109045/numpy-where-with-multiple-conditions -> answer #2
#  sqlite3.connect must have '../' before db file in order to navigate up one directory when running in terminal, but NOT for view in browser

def highlight_max(cell): 
    if type(cell) == str:
        return 'background: white; color: black' #; border: 1px solid black
    if type(cell) != str and cell < 0 : 
        return 'background: blue; color:black'
    else: 
        return 'background: green; color: white'
# Using apply method of style  
# attribute of Pandas DataFrame 

def accurate_wl(request):
    # merge actual and predited spreads
    dd = get_df_panda().reset_index(drop = True)
    dd = dd.loc[:16,['Title','Differenchy']]
    df_predictions = pd.read_sql('SELECT * FROM vPredicted_Score_Dif', sqlite3.connect('db.sqlite3'))
    df_predictions = df_predictions.T
    new_header = df_predictions.iloc[0] #grab the first row for the header
    df_predictions = df_predictions[1:] #take the data less the header row
    df_predictions.columns = new_header #set the header row as the df header
    df_predictions = df_predictions.reset_index(drop = True)
    bigdata = pd.merge(dd, df_predictions, left_index=True, right_index=True)
    bigdata = bigdata.fillna(0)
    bigdata['Differenchy'] = bigdata['Differenchy'].astype(int)
    bigdata = bigdata.rename(columns={'Differenchy' : 'Actual Spread'})
    bigdatahtml = bigdata.to_html(classes="table table-striped table-bordered table-hover", index=False)
    # show accuracy of predictions
    dumb=[]
    for index, row in bigdata.iterrows():
        zz = np.where((row[1] * row[2:]) > 0, (row[1] - row[2:]).abs(), None).tolist()
        zz.insert(0,row[1])
        zz.insert(0,row[0])
        dumb.append(zz)
    dumb = np.array(dumb)
    df_accurate_wl = pd.DataFrame(dumb, columns=bigdata.columns.to_list()).fillna('X')
    df_accurate_wlhtml = df_accurate_wl.style.applymap(highlight_max).hide_index().set_table_attributes('border="1" class="dataframe table table-hover table-bordered table-striped"').render()
    # # prediction grade
    # df_accurate_wl_funk = df_accurate_wl
    # cut_conditions = [-1, 0, 3.5, 7.5, 10.5, 14.5, 21.5,22]
    # cut_scores =     [    1, .95,  .9,  .85,   .8, .75, 0]
    # df_predictions_accuracy = pd.DataFrame()
    # df_predictions_accuracy['name'] = df_accurate_wl.iloc[:,0]
    # df_predictions_accuracy['WEEK1'] = pd.cut(df_accurate_wl_funk['WEEK1'],bins = cut_conditions, labels = cut_scores, include_lowest=True, right=True)
    return render(request, "seahawks_2022_predictions/accuracy.html", {'df_accurate_wl': df_accurate_wlhtml, 'df_predictions': df_predictions.to_html(), 'bigdata' : bigdatahtml })
