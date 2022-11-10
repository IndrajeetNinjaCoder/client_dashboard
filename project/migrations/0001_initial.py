# Generated by Django 4.0.3 on 2022-11-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('priority', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('_from', models.DateField()),
                ('_to', models.DateField()),
                ('work_status', models.CharField(max_length=255)),
            ],
        ),
    ]
