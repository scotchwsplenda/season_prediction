from django.urls import path
from django.contrib import admin
from .views import  hawks_predictions_view, hawks_scores_view, submitted_predictions

urlpatterns = [
    path('form/', hawks_predictions_view, name="whatisthis"),
    path('scores/', hawks_scores_view),
    path('predictions/', submitted_predictions)

    # path('submissions/', submitted_predictions.as_view(), name = 'hopeless')
]