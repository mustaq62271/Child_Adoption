# Generated by Django 3.1.7 on 2021-08-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0009_auto_20210821_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childtable',
            name='address',
        ),
        migrations.RemoveField(
            model_name='childtable',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='childtable',
            name='district',
        ),
        migrations.RemoveField(
            model_name='childtable',
            name='division',
        ),
        migrations.AddField(
            model_name='childtable',
            name='image',
            field=models.ImageField(default=20, upload_to='media/childimage/'),
            preserve_default=False,
        ),
    ]