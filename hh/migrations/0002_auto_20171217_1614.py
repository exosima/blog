# Generated by Django 2.0 on 2017-12-17 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hh', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='po',
            old_name='posts',
            new_name='context',
        ),
    ]