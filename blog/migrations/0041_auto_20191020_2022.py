# Generated by Django 2.2 on 2019-10-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20191020_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='mobile_number',
            field=models.CharField(default=None, max_length=10, verbose_name='Mobile_number'),
        ),
    ]