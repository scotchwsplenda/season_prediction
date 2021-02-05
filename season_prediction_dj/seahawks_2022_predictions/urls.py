from django.urls import path
from django.contrib import admin
from .views import  hawks_predictions_form, hawks_scores_view, accurate_wl

urlpatterns = [
    path('form/', hawks_predictions_form ), # , name="you can name your page for reference elsewhere"
    path('', hawks_scores_view),
    path('accuracy/', accurate_wl)


    # path('submissions/', submitted_predictions.as_view(), name = 'hopeless')
]