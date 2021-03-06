# Generated by Django 3.2.4 on 2021-06-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegForm',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('aadhar', models.IntegerField()),
                ('fname', models.CharField(max_length=60)),
                ('foccupation', models.CharField(max_length=60)),
                ('institutename', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=60)),
                ('presentyear', models.CharField(max_length=60)),
                ('percentage12', models.CharField(max_length=60)),
                ('cgpa', models.CharField(max_length=60)),
                ('photograph', models.ImageField(default='', upload_to='Photographs')),
                ('marksheet12', models.FileField(default='', upload_to='Marksheets_12')),
                ('lmarksheet', models.FileField(default='', upload_to='Latest_Marksheets')),
                ('bletter', models.FileField(default='', upload_to='Bonafied_Letters')),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
    ]
