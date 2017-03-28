# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column=b'name', max_length=50)),
                ('surname', models.CharField(db_column=b'surname', max_length=50)),
                ('location', models.CharField(db_column=b'location', max_length=50, null=True)),
                ('region', models.CharField(db_column=b'region', max_length=50, null=True)),
                ('zipCode', models.IntegerField(db_column=b'zip_code', null=True)),
                ('mail', models.EmailField(db_column=b'mail', max_length=100, null=True)),
            ],
        ),
    ]
