# Generated by Django 4.2.3 on 2023-07-27 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankApp', '0002_rename_name_branches_br_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='bank_id',
        ),
    ]