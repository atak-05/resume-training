# Generated by Django 4.2.4 on 2023-08-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_generalsetting_description_generalsetting_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
