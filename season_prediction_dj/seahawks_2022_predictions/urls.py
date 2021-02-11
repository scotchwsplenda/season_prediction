from django.urls import path
from django.contrib import admin
from .views import  hawks_predictions_form, hawks_scores_view, accurate_wl
from django.views.generic import TemplateView

urlpatterns = [
    path('form/', hawks_predictions_form ), # , name="you can name your page for reference elsewhere"
    path('', hawks_scores_view),
    path('accuracy/', accurate_wl),
    path('howitworks/', TemplateView.as_view(template_name='seahawks_2022_predictions/how_it_works.html'))

    # path('submissions/', submitted_predictions.as_view(), name = 'hopeless')
]