# Generated by Django 3.0.7 on 2020-08-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortify', '0002_auto_20200805_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltab',
            name='longurl',
            field=models.CharField(max_length=250),
        ),
    ]
