# Generated by Django 2.2 on 2019-09-24 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190924_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_job', models.CharField(max_length=100, verbose_name='Job Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('Job_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-Job_date',),
            },
        ),
    ]
