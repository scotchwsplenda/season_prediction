from django.shortcuts import render, redirect, HttpResponse
from .forms import prediction_form
from .hawksscore import get_df_panda
from .models import prediction_table
from django_pandas.io import read_frame
import pandas as pd
import sqlite3

# Create your views here.

def hawks_predictions_view(request):
    form = prediction_form()

    season2 = get_df_panda()

    if request.method == "POST":
        form = prediction_form(request.POST)
        print(form)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('/scores')

    return render(request, "seahawks_2022_predictions/predictions.html", {'form': form, 'season': season2})

def hawks_scores_view(request):
    return HttpResponse(get_df_panda().to_html())

def submitted_predictions(request):
    qs = prediction_table.objects.all()
    df = read_frame(qs)
    return HttpResponse(df.to_html())

def submitted_predictions_dif(request):
    df = pd.read_sql('SELECT id, name, Predicted_HawkScore_Wk1 -  Predicted_OppScore_Wk1 as Predicted_Wk1_Score_Dif, Predicted_HawkScore_Wk2 -  Predicted_OppScore_Wk2 as Predicted_Wk2_Score_Dif, Predicted_HawkScore_Wk3 -  Predicted_OppScore_Wk3 as Predicted_Wk3_Score_Dif, Predicted_HawkScore_Wk4 -  Predicted_OppScore_Wk4 as Predicted_Wk4_Score_Dif, Predicted_HawkScore_Wk5 -  Predicted_OppScore_Wk5 as Predicted_Wk5_Score_Dif, Predicted_HawkScore_Wk6 -  Predicted_OppScore_Wk6 as Predicted_Wk6_Score_Dif, Predicted_HawkScore_Wk7 -  Predicted_OppScore_Wk7 as Predicted_Wk7_Score_Dif, Predicted_HawkScore_Wk8 -  Predicted_OppScore_Wk8 as Predicted_Wk8_Score_Dif, Predicted_HawkScore_Wk9 -  Predicted_OppScore_Wk9 as Predicted_Wk9_Score_Dif, Predicted_HawkScore_Wk10 - Predicted_OppScore_Wk10 as Predicted_Wk10_Score_Dif, Predicted_HawkScore_Wk11 - Predicted_OppScore_Wk11 as Predicted_Wk11_Score_Dif, Predicted_HawkScore_Wk12 - Predicted_OppScore_Wk12 as Predicted_Wk12_Score_Dif, Predicted_HawkScore_Wk13 - Predicted_OppScore_Wk13 as Predicted_Wk13_Score_Dif, Predicted_HawkScore_Wk14 - Predicted_OppScore_Wk14 as Predicted_Wk14_Score_Dif, Predicted_HawkScore_Wk15 - Predicted_OppScore_Wk15 as Predicted_Wk15_Score_Dif, Predicted_HawkScore_Wk16 - Predicted_OppScore_Wk16 as Predicted_Wk16_Score_Dif, Predicted_HawkScore_Wk17 - Predicted_OppScore_Wk17 as Predicted_Wk17_Score_Dif FROM seahawks_2022_predictions_prediction_table', sqlite3.connect('db.sqlite3'))
    return HttpResponse(df.to_html())


print()

# df_predictions = pd.read_sql('SELECT id, name, Predicted_HawkScore_Wk1 -  Predicted_OppScore_Wk1 as Predicted_Wk1_Score_Dif, Predicted_HawkScore_Wk2 -  Predicted_OppScore_Wk2 as Predicted_Wk2_Score_Dif, Predicted_HawkScore_Wk3 -  Predicted_OppScore_Wk3 as Predicted_Wk3_Score_Dif, Predicted_HawkScore_Wk4 -  Predicted_OppScore_Wk4 as Predicted_Wk4_Score_Dif, Predicted_HawkScore_Wk5 -  Predicted_OppScore_Wk5 as Predicted_Wk5_Score_Dif, Predicted_HawkScore_Wk6 -  Predicted_OppScore_Wk6 as Predicted_Wk6_Score_Dif, Predicted_HawkScore_Wk7 -  Predicted_OppScore_Wk7 as Predicted_Wk7_Score_Dif, Predicted_HawkScore_Wk8 -  Predicted_OppScore_Wk8 as Predicted_Wk8_Score_Dif, Predicted_HawkScore_Wk9 -  Predicted_OppScore_Wk9 as Predicted_Wk9_Score_Dif, Predicted_HawkScore_Wk10 - Predicted_OppScore_Wk10 as Predicted_Wk10_Score_Dif, Predicted_HawkScore_Wk11 - Predicted_OppScore_Wk11 as Predicted_Wk11_Score_Dif, Predicted_HawkScore_Wk12 - Predicted_OppScore_Wk12 as Predicted_Wk12_Score_Dif, Predicted_HawkScore_Wk13 - Predicted_OppScore_Wk13 as Predicted_Wk13_Score_Dif, Predicted_HawkScore_Wk14 - Predicted_OppScore_Wk14 as Predicted_Wk14_Score_Dif, Predicted_HawkScore_Wk15 - Predicted_OppScore_Wk15 as Predicted_Wk15_Score_Dif, Predicted_HawkScore_Wk16 - Predicted_OppScore_Wk16 as Predicted_Wk16_Score_Dif, Predicted_HawkScore_Wk17 - Predicted_OppScore_Wk17 as Predicted_Wk17_Score_Dif FROM seahawks_2022_predictions_prediction_table', sqlite3.connect('db.sqlite3'))
#  ['Week','Day','Date','Time','Result','OT','Rec',
#  'Home_Away','Opp','HawkScore','OppScore', 'Differenchy', 'Title']

