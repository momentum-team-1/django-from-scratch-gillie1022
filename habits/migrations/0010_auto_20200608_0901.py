# Generated by Django 3.0.6 on 2020-06-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0009_auto_20200608_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='recorded_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
