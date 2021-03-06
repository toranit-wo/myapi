# Generated by Django 3.2.3 on 2021-08-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('data', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Backhand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('tmor', models.FloatField(default=0)),
                ('cra', models.FloatField(default=0)),
                ('tmcr', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Forehand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('tmor', models.FloatField(default=0)),
                ('cra', models.FloatField(default=0)),
                ('tmcr', models.FloatField(default=0)),
            ],
        ),
    ]
