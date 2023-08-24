# Generated by Django 4.1.7 on 2023-08-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateField(auto_now_add=True, verbose_name='updated date')),
                ('created_date', models.DateField(auto_now=True, verbose_name='created date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('file', models.FileField(blank=True, default='', max_length=254, upload_to='documents/', verbose_name='File')),
                ('button_text', models.CharField(blank=True, default='', max_length=254, verbose_name='Button Text')),
                ('slug', models.SlugField(blank=True, default='', max_length=254, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'DocumentS',
                'ordering': ('order',),
            },
        ),
    ]