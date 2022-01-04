# Generated by Django 3.2.8 on 2021-12-27 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cnc', '0004_careerapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='published_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='product_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='cnc.product'),
        ),
    ]
