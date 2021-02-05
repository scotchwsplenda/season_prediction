from django.shortcuts import render, redirect
from .forms import prediction_form
from .hawksscore import get_df_panda

import pandas as pd
import sqlite3
import numpy as np
# Create your views here.

def hawks_predictions_form(request):
    form = prediction_form()

    season2 = get_df_panda()

    if request.method == "POST":
        form = prediction_form(request.POST)
        print(form)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('/scores')

    return render(request, "seahawks_2022_predictions/form.html", {'form': form, 'season': season2})

def hawks_scores_view(request):
    return render(request, "seahawks_2022_predictions/home.html", {'get_df_panda': get_df_panda().to_html()})


# https://stackoverflow.com/questions/39109045/numpy-where-with-multiple-conditions -> answer #2
#  sqlite3.connect must have '../' before db file in order to navigate up one directory when running in terminal, but NOT for view in browser
def accurate_wl(request):
    # table for predicted spread
    df_predictions = pd.read_sql('SELECT id, name, Predicted_HawkScore_Wk1 -  Predicted_OppScore_Wk1 as Predicted_Wk1_Spred, Predicted_HawkScore_Wk2 -  Predicted_OppScore_Wk2 as Predicted_Wk2_Spred, Predicted_HawkScore_Wk3 -  Predicted_OppScore_Wk3 as Predicted_Wk3_Spred, Predicted_HawkScore_Wk4 -  Predicted_OppScore_Wk4 as Predicted_Wk4_Spred, Predicted_HawkScore_Wk5 -  Predicted_OppScore_Wk5 as Predicted_Wk5_Spred, Predicted_HawkScore_Wk6 -  Predicted_OppScore_Wk6 as Predicted_Wk6_Spred, Predicted_HawkScore_Wk7 -  Predicted_OppScore_Wk7 as Predicted_Wk7_Spred, Predicted_HawkScore_Wk8 -  Predicted_OppScore_Wk8 as Predicted_Wk8_Spred, Predicted_HawkScore_Wk9 -  Predicted_OppScore_Wk9 as Predicted_Wk9_Spred, Predicted_HawkScore_Wk10 - Predicted_OppScore_Wk10 as Predicted_Wk10_Spred, Predicted_HawkScore_Wk11 - Predicted_OppScore_Wk11 as Predicted_Wk11_Spred, Predicted_HawkScore_Wk12 - Predicted_OppScore_Wk12 as Predicted_Wk12_Spred, Predicted_HawkScore_Wk13 - Predicted_OppScore_Wk13 as Predicted_Wk13_Spred, Predicted_HawkScore_Wk14 - Predicted_OppScore_Wk14 as Predicted_Wk14_Spred, Predicted_HawkScore_Wk15 - Predicted_OppScore_Wk15 as Predicted_Wk15_Spred, Predicted_HawkScore_Wk16 - Predicted_OppScore_Wk16 as Predicted_Wk16_Spred, Predicted_HawkScore_Wk17 - Predicted_OppScore_Wk17 as Predicted_Wk17_Spred FROM seahawks_2022_predictions_prediction_table;', sqlite3.connect('db.sqlite3'))
    funky = get_df_panda()
    # table for difference between predicted and actual spread
    df_accurate_wl = pd.DataFrame()
    df_accurate_wl['Name'] = df_predictions['name']
    df_accurate_wl['WEEK1'] = np.where(
        ((df_predictions['Predicted_Wk1_Spred'] * funky['Differenchy'][0]) > 0), # correctly predicted W/L 
         (df_predictions['Predicted_Wk1_Spred'] - funky['Differenchy'][0]).abs(),'WRONG') # dif between actual and predicted, (if W/L wrong -1)
    df_accurate_wl['WEEK2'] = np.where(
        ((df_predictions['Predicted_Wk2_Spred'] * funky['Differenchy'][1]) > 0), 
         (df_predictions['Predicted_Wk2_Spred'] - funky['Differenchy'][1]).abs(),'WRONG') 
    df_accurate_wl['WEEK3'] = np.where(
        ((df_predictions['Predicted_Wk3_Spred'] * funky['Differenchy'][2]) > 0), 
         (df_predictions['Predicted_Wk3_Spred'] - funky['Differenchy'][2]).abs(),'WRONG') 
    df_accurate_wl['WEEK4'] = np.where(
        ((df_predictions['Predicted_Wk4_Spred'] * funky['Differenchy'][3]) > 0),
         (df_predictions['Predicted_Wk4_Spred'] - funky['Differenchy'][3]).abs(),'WRONG') 
    df_accurate_wl['WEEK5'] = np.where(
        ((df_predictions['Predicted_Wk5_Spred'] * funky['Differenchy'][4]) > 0), 
         (df_predictions['Predicted_Wk5_Spred'] - funky['Differenchy'][4]).abs(),'WRONG') 
    return render(request, "seahawks_2022_predictions/accuracy.html", {'df_accurate_wl': df_accurate_wl.to_html(), 'df_predictions': df_predictions.to_html() })

