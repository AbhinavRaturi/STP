# Generated by Django 3.2.4 on 2021-06-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StpApp', '0002_alter_regform_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='aadhar',
            field=models.BigIntegerField(),
        ),
    ]
