# Generated by Django 2.2 on 2019-09-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190930_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='uploads_cv',
            field=models.FileField(default='NULL', upload_to='upload_cv', verbose_name='Uploads CV'),
        ),
    ]
