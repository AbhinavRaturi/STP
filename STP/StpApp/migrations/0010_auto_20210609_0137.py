# Generated by Django 3.2.4 on 2021-06-08 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StpApp', '0009_auto_20210608_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studdata',
            name='R1Marks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='studdata',
            name='R2Marks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='studdata',
            name='R3Marks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='studdata',
            name='StudTotal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]