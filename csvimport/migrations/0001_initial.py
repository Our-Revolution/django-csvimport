# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-14 16:03
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default=b'csvimport.Item', help_text=b'Please specify the app_label.model_name', max_length=255)),
                ('field_list', models.TextField(blank=True, help_text=b'Enter list of fields in order only if\n                                     you dont have a header row with matching field names, eg.\n                                     "column1=shared_code,column2=org(Organisation|name)"')),
                ('upload_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=''), upload_to=b'csv')),
                ('file_name', models.CharField(blank=True, max_length=255)),
                ('encoding', models.CharField(blank=True, max_length=32)),
                ('upload_method', models.CharField(choices=[(b'manual', b'manual'), (b'cronjob', b'cronjob')], default=b'manual', max_length=50)),
                ('error_log', models.TextField(help_text=b'Each line is an import error')),
                ('import_date', models.DateField(auto_now=True)),
                ('import_user', models.CharField(blank=True, default=b'anonymous', help_text=b'User id as text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ImportModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeric_id', models.PositiveIntegerField()),
                ('natural_key', models.CharField(max_length=100)),
                ('csvimport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csvimport.CSVImport')),
            ],
        ),
    ]
