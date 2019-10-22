# Generated by Django 2.2 on 2019-10-20 13:22

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20191020_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='mobile_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
