# Generated by Django 3.1.7 on 2021-08-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='childtable',
            name='childid',
            field=models.CharField(default=50, max_length=10),
            preserve_default=False,
        ),
    ]
