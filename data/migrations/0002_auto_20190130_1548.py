# Generated by Django 2.1.5 on 2019-01-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='name',
            field=models.SlugField(primary_key=True, serialize=False),
        ),
    ]
