# Generated by Django 2.1.5 on 2019-01-30 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('greeting', models.CharField(max_length=200)),
            ],
        ),
    ]
