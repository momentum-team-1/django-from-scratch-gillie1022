# Generated by Django 3.0.6 on 2020-06-02 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='goal_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='noun',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='habit',
            name='verb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
