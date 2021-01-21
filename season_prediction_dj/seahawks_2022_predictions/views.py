from django.shortcuts import render, redirect, HttpResponse
from .forms import prediction_form
from .hawksscore import get_df_panda
from .models import prediction_table

# Create your views here.

# Create your views here. test
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
    return HttpResponse(prediction_table.to_html())