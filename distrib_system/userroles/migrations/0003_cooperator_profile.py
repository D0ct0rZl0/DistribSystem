# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 07:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userroles.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('userroles', '0002_auto_20170708_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('password', models.CharField(max_length=16, verbose_name='Пароль')),
                ('work', models.CharField(max_length=50, verbose_name='Специализация')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', userroles.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('cooperator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userroles.Cooperator', verbose_name='Сотрудник')),
            ],
        ),
    ]
