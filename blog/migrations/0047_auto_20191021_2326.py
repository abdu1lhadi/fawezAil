# Generated by Django 2.2 on 2019-10-21 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_auto_20191021_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='mobile_number',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Mobile_number'),
        ),
    ]
