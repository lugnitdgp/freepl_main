# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-16 10:08
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country1', models.TextField(default='', max_length=100)),
                ('country2', models.TextField(default='', max_length=100)),
                ('day', models.DateField(default=datetime.datetime(2018, 9, 16, 10, 8, 57, 136822))),
                ('can_edit', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'match',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('total_score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='PersontoPM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_player', models.BooleanField(default=False)),
                ('score', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Person')),
            ],
            options={
                'db_table': 'person_PM',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', max_length=30)),
                ('country', models.TextField(default='', max_length=100)),
                ('cost', models.IntegerField(default=0)),
                ('role', models.TextField(default='', max_length=25)),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='PlayertoMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Player')),
            ],
            options={
                'db_table': 'PlayertoMatch',
            },
        ),
        migrations.AddField(
            model_name='persontopm',
            name='pm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.PlayertoMatch'),
        ),
    ]
