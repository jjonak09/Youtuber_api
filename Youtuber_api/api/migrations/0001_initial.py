# Generated by Django 2.1.5 on 2019-01-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('belong', models.CharField(max_length=30)),
                ('twiiter', models.CharField(max_length=30)),
                ('channel_id', models.CharField(max_length=60)),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('belong', models.CharField(max_length=30)),
                ('twiiter', models.CharField(max_length=40)),
                ('channel_id', models.CharField(max_length=60)),
                ('tag', models.CharField(max_length=30)),
            ],
        ),
    ]
