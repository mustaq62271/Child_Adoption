# Generated by Django 3.1.7 on 2021-08-20 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0006_auto_20210820_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childtable',
            old_name='childcode',
            new_name='childid',
        ),
    ]
