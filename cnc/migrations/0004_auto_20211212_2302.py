# Generated by Django 3.2.8 on 2021-12-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnc', '0003_auto_20211212_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='model_numbeer',
        ),
        migrations.AddField(
            model_name='product',
            name='model_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]