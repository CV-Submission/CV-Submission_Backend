# Generated by Django 3.0.8 on 2021-06-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVprofileSubmission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetials',
            name='MobileNumber',
            field=models.IntegerField(unique=True),
        ),
    ]