# Generated by Django 4.1.7 on 2023-08-21 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('name',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]
