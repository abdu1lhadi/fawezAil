# Generated by Django 2.2 on 2019-10-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20191021_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='mobile_number',
            field=models.CharField(default=None, max_length=12, verbose_name='Mobile_number'),
        ),
    ]