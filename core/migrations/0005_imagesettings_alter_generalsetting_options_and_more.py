# Generated by Django 4.2.4 on 2023-08-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_generalsetting_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of setting.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('file', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='Image')),
            ],
        ),
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='created_date',
            field=models.DateField(auto_now=True, verbose_name='created date'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(default='', help_text='this is variable of settings', max_length=254, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameters',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='parameters'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_date',
            field=models.DateField(auto_now_add=True, verbose_name='updated date'),
        ),
    ]
