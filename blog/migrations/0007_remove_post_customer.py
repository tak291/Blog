# Generated by Django 3.1.5 on 2021-02-11 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210211_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='customer',
        ),
    ]
