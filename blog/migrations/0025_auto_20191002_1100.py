# Generated by Django 2.2 on 2019-10-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20191002_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequest',
            name='uploaad_cv',
            field=models.FileField(null=True, upload_to='upload_cv'),
        ),
    ]