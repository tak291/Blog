# Generated by Django 3.1.5 on 2021-02-11 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210211_0349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='addr',
            new_name='addres',
        ),
    ]