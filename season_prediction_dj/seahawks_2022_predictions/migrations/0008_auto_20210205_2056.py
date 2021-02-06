# Generated by Django 3.1.3 on 2021-02-06 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seahawks_2022_predictions', '0007_remove_prediction_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction_table',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
