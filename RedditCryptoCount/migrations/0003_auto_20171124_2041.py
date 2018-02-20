# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedditCryptoCount', '0002_auto_20171124_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckedPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=301)),
            ],
        ),
        migrations.CreateModel(
            name='ThisCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_id', models.CharField(max_length=256)),
                ('coin_symbol', models.CharField(max_length=16)),
                ('count', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='TempCount',
        ),
        migrations.AlterField(
            model_name='lastcount',
            name='lastcount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lastcount',
            name='pc_diff',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
