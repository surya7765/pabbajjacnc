# Generated by Django 3.2.8 on 2021-12-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='gmail',
        ),
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.CharField(max_length=250),
        ),
    ]
