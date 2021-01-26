from django.urls import path
from django.contrib import admin
from .views import  hawks_predictions_view, hawks_scores_view, submitted_predictions, submitted_predictions_dif

urlpatterns = [
    path('form/', hawks_predictions_view, name="whatisthis"),
    path('', hawks_scores_view),
    path('scores/', hawks_scores_view),
    path('predictions/', submitted_predictions),
    path('predicted_difs/', submitted_predictions_dif)

    # path('submissions/', submitted_predictions.as_view(), name = 'hopeless')
]