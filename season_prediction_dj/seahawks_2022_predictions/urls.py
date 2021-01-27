from django.urls import path
from django.contrib import admin
from .views import  hawks_predictions_view, hawks_scores_view, submitted_predictions, accurate_wl

urlpatterns = [
    path('form/', hawks_predictions_view, name="whatisthis"),
    path('', accurate_wl),
    path('scores/', hawks_scores_view),
    path('predictions/', submitted_predictions),
    path('accuracy/', accurate_wl)


    # path('submissions/', submitted_predictions.as_view(), name = 'hopeless')
]