# Generated by Django 4.2.4 on 2023-08-16 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='parameters',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='updated_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
