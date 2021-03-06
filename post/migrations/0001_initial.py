# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-13 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Resim')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
            ],
            options={
                'ordering': ['-publishing_date', 'id'],
            },
        ),
    ]
