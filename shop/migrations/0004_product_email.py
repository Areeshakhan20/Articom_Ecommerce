# Generated by Django 3.0.7 on 2020-08-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200811_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
    ]