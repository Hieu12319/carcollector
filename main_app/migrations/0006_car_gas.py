# Generated by Django 4.0.6 on 2022-07-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_gas_alter_maintenance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='gas',
            field=models.ManyToManyField(to='main_app.gas'),
        ),
    ]
