# Generated by Django 2.2 on 2019-10-02 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20191001_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobrequest',
            options={},
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='certificate',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='name_employee',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='name_job',
        ),
        migrations.RemoveField(
            model_name='jobrequest',
            name='post_date',
        ),
    ]
