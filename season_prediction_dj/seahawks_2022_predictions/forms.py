from .models import prediction_table
from django.forms import ModelForm


class prediction_form(ModelForm):
    class Meta:
        model = prediction_table
        fields = '__all__'
        exclude = ('author',)