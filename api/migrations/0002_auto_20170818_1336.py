# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('contenu', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date posted')),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Centres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=255)),
                ('long', models.CharField(max_length=255)),
                ('qteDisponible', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critere', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date posted')),
                ('pourcentage', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Api',
        ),
    ]
