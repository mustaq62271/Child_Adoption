# Generated by Django 3.1.7 on 2021-08-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0008_auto_20210820_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childtable',
            old_name='district',
            new_name='blood',
        ),
        migrations.RenameField(
            model_name='childtable',
            old_name='division',
            new_name='childage',
        ),
        migrations.RemoveField(
            model_name='childtable',
            name='address',
        ),
        migrations.RemoveField(
            model_name='childtable',
            name='contact',
        ),
        migrations.AddField(
            model_name='childtable',
            name='childheight',
            field=models.CharField(default=4, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childtable',
            name='childweight',
            field=models.CharField(default=5, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childtable',
            name='gender',
            field=models.CharField(default=7, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childtable',
            name='health',
            field=models.CharField(default=8, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='childtable',
            name='image',
            field=models.ImageField(default=10, upload_to='media/childimage/'),
            preserve_default=False,
        ),
    ]