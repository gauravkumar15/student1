# Generated by Django 2.1 on 2018-09-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Roll_no', models.CharField(max_length=20)),
                ('Father_name', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=20)),
                ('Address', models.TextField()),
            ],
        ),
    ]
