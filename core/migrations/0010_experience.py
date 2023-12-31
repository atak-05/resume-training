# Generated by Django 4.1.7 on 2023-08-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_skill_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='updated date')),
                ('created_date', models.DateField(auto_now=True, verbose_name='created date')),
                ('company_name', models.CharField(blank=True, default='', max_length=254, verbose_name='Company Name')),
                ('job_title', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Title')),
                ('job_location', models.CharField(blank=True, default='', max_length=254, verbose_name='Job Location')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(default=None, null=True, verbose_name='End Date')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
                'ordering': ('start_date',),
            },
        ),
    ]
