# Generated by Django 2.2 on 2019-10-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_auto_20191024_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='nopersnt',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Mobile Number'),
        ),
    ]
