# Generated by Django 2.2.7 on 2019-12-23 10:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.FloatField(default=0)),
                ('take_into_account', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('planned', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('date', models.DateField(default=datetime.datetime(2019, 12, 23, 10, 21, 15, 702517, tzinfo=utc))),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.Account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Category')),
                ('label', models.ManyToManyField(blank=True, null=True, to='wallet.Label')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.datetime(2019, 12, 23, 10, 21, 15, 701520, tzinfo=utc))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Account')),
            ],
        ),
    ]
