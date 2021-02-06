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
def accurate_wl(request):
    # table for pred spread
    df_predictions = pd.read_sql('SELECT * FROM vPredicted_Score_Dif', sqlite3.connect('db.sqlite3'))
    funky = get_df_panda()
    # table for difference between predicted and actual spread
    df_accurate_wl = pd.DataFrame()
    df_accurate_wl['Name'] = df_predictions['username']
    df_accurate_wl['WEEK1'] = np.where(
        ((df_predictions['Pred_Wk1_Spred'] * funky['Differenchy'][0]) > 0), # correctly predicted W/L 
         (df_predictions['Pred_Wk1_Spred'] - funky['Differenchy'][0]).abs(),'WRONG') # dif between actual and predicted, (if W/L wrong -1)
    df_accurate_wl['WEEK2'] = np.where(
        ((df_predictions['Pred_Wk2_Spred'] * funky['Differenchy'][1]) > 0), 
         (df_predictions['Pred_Wk2_Spred'] - funky['Differenchy'][1]).abs(),'WRONG') 
    df_accurate_wl['WEEK3'] = np.where(
        ((df_predictions['Pred_Wk3_Spred'] * funky['Differenchy'][2]) > 0), 
         (df_predictions['Pred_Wk3_Spred'] - funky['Differenchy'][2]).abs(),'WRONG') 
    df_accurate_wl['WEEK4'] = np.where(
        ((df_predictions['Pred_Wk4_Spred'] * funky['Differenchy'][3]) > 0),
         (df_predictions['Pred_Wk4_Spred'] - funky['Differenchy'][3]).abs(),'WRONG') 
    df_accurate_wl['WEEK5'] = np.where(
        ((df_predictions['Pred_Wk5_Spred'] * funky['Differenchy'][4]) > 0), 
         (df_predictions['Pred_Wk5_Spred'] - funky['Differenchy'][4]).abs(),'WRONG') 
    df_accurate_wl['WEEK6'] = np.where(
        ((df_predictions['Pred_Wk6_Spred'] * funky['Differenchy'][5]) > 0), 
         (df_predictions['Pred_Wk6_Spred'] - funky['Differenchy'][5]).abs(),'WRONG') 
    df_accurate_wl['WEEK7'] = np.where(
        ((df_predictions['Pred_Wk7_Spred'] * funky['Differenchy'][6]) > 0), 
         (df_predictions['Pred_Wk7_Spred'] - funky['Differenchy'][6]).abs(),'WRONG') 
    df_accurate_wl['WEEK8'] = np.where(
        ((df_predictions['Pred_Wk8_Spred'] * funky['Differenchy'][7]) > 0),
         (df_predictions['Pred_Wk8_Spred'] - funky['Differenchy'][7]).abs(),'WRONG') 
    df_accurate_wl['WEEK9'] = np.where(
        ((df_predictions['Pred_Wk9_Spred'] * funky['Differenchy'][8]) > 0), 
         (df_predictions['Pred_Wk9_Spred'] - funky['Differenchy'][8]).abs(),'WRONG') 
    df_accurate_wl['WEEK10'] = np.where(
        ((df_predictions['Pred_Wk10_Spred'] * funky['Differenchy'][9]) > 0), 
         (df_predictions['Pred_Wk10_Spred'] - funky['Differenchy'][9]).abs(),'WRONG') 
    df_accurate_wl['WEEK11'] = np.where(
        ((df_predictions['Pred_Wk11_Spred'] * funky['Differenchy'][10]) > 0), 
         (df_predictions['Pred_Wk11_Spred'] - funky['Differenchy'][10]).abs(),'WRONG') 
    df_accurate_wl['WEEK12'] = np.where(
        ((df_predictions['Pred_Wk12_Spred'] * funky['Differenchy'][11]) > 0),
         (df_predictions['Pred_Wk12_Spred'] - funky['Differenchy'][11]).abs(),'WRONG') 
    df_accurate_wl['WEEK13'] = np.where(
        ((df_predictions['Pred_Wk13_Spred'] * funky['Differenchy'][12]) > 0), 
         (df_predictions['Pred_Wk13_Spred'] - funky['Differenchy'][12]).abs(),'WRONG') 
    df_accurate_wl['WEEK14'] = np.where(
        ((df_predictions['Pred_Wk14_Spred'] * funky['Differenchy'][13]) > 0), 
         (df_predictions['Pred_Wk14_Spred'] - funky['Differenchy'][13]).abs(),'WRONG') 
    df_accurate_wl['WEEK15'] = np.where(
        ((df_predictions['Pred_Wk15_Spred'] * funky['Differenchy'][14]) > 0), 
         (df_predictions['Pred_Wk15_Spred'] - funky['Differenchy'][14]).abs(),'WRONG') 
    df_accurate_wl['WEEK16'] = np.where(
        ((df_predictions['Pred_Wk16_Spred'] * funky['Differenchy'][15]) > 0),
         (df_predictions['Pred_Wk16_Spred'] - funky['Differenchy'][15]).abs(),'WRONG') 
    df_accurate_wl['WEEK17'] = np.where(
        ((df_predictions['Pred_Wk17_Spred'] * funky['Differenchy'][16]) > 0), 
         (df_predictions['Pred_Wk17_Spred'] - funky['Differenchy'][16]).abs(),'WRONG')
    return render(request, "seahawks_2022_predictions/accuracy.html", {'df_accurate_wl': df_accurate_wl.to_html(), 'df_predictions': df_predictions.to_html() })

