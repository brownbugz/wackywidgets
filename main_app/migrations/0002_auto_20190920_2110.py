# Generated by Django 2.2.3 on 2019-09-20 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
