# Generated by Django 3.2.8 on 2022-01-05 12:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('image_url', models.CharField(blank=True, max_length=500)),
                ('job_location', models.CharField(max_length=50)),
                ('job_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('responsibility', tinymce.models.HTMLField(blank=True, null=True)),
                ('skillset', tinymce.models.HTMLField(blank=True, null=True)),
                ('additional', tinymce.models.HTMLField(blank=True, null=True)),
                ('internship', models.BooleanField(default=False, verbose_name='Internship')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_contact', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Give your title')),
                ('price', models.CharField(max_length=10, verbose_name='Enter Price')),
                ('availability', models.BooleanField(verbose_name='Available or Not')),
                ('model_number', models.CharField(blank=True, max_length=50)),
                ('video_url', models.URLField(max_length=300, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='upload/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='upload/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='upload/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('automatic', models.BooleanField(default=False, verbose_name='Automatic or Manual')),
                ('weight', models.CharField(blank=True, max_length=50)),
                ('plc_control', models.BooleanField(default=False, verbose_name='PLC Control')),
                ('computerized', models.BooleanField(default=False, verbose_name='Computerized or Manual')),
                ('supply_ability', models.BooleanField(default=False, verbose_name='Supply Ability')),
                ('detail', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=250)),
                ('gmail', models.EmailField(max_length=50)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('image', models.ImageField(null=True, upload_to='upload/')),
            ],
        ),
        migrations.CreateModel(
            name='CareerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gmail_id', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=50)),
                ('date_upload', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('contact_details', models.TextField(blank=True, verbose_name='Contact Details')),
                ('resume', models.FileField(blank=True, upload_to='upload/')),
                ('career', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cnc.career')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_book', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('message', models.TextField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cnc.product')),
            ],
        ),
    ]
