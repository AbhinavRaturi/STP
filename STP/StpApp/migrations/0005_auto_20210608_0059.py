# Generated by Django 3.2.4 on 2021-06-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StpApp', '0004_tupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tupload',
            name='treview1',
            field=models.FileField(null=True, upload_to='treview1'),
        ),
        migrations.AlterField(
            model_name='tupload',
            name='treview2',
            field=models.FileField(null=True, upload_to='treview2'),
        ),
        migrations.AlterField(
            model_name='tupload',
            name='treview3',
            field=models.FileField(null=True, upload_to='treview3'),
        ),
    ]
