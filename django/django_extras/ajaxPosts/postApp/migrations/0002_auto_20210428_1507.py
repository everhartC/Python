# Generated by Django 3.1.6 on 2021-04-28 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='last_name',
        ),
    ]