# Generated by Django 2.2 on 2019-10-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20191020_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='mobile_number',
            field=models.IntegerField(default=None, max_length=10, verbose_name='mobile_number'),
        ),
    ]