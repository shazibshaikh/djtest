# Generated by Django 2.1.2 on 2018-10-15 13:50

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('post_nominals', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6)),
            ],
        ),
    ]
