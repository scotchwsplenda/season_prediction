from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
# from django.db.models.fields import related


# https://docs.djangoproject.com/en/3.1/howto/legacy-databases/ -> python manage.py inspectdb
# https://datatofish.com/pandas-dataframe-to-sql/
# Create your models here.
# install SQLITE Explorer extension

class prediction_table(models.Model):
    # username= models.ForeignKey(User, to_field=User.username, on_delete=models.CASCADE)
    # name = models.ForeignKey(get_user_model(), to_field=User.username, on_delete=models.CASCADE, null=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    Predicted_HawkScore_Wk1= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk1= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk2= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk2= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk3= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk3= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk4= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk4= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk5= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk5= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk6= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk6= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk7= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk7= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk8= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk8=models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk9= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk9= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk10= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk10= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk11= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk11= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk12= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk12= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk13= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk13= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk14= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk14= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk15= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk15= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk16= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk16= models.PositiveIntegerField(default=0)
    Predicted_HawkScore_Wk17= models.PositiveIntegerField(default=0)
    Predicted_OppScore_Wk17= models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name