# Generated by Django 3.2.4 on 2021-06-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StpApp', '0007_auto_20210608_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='studdata',
            name='StudUsername',
            field=models.CharField(default='17STU0666', max_length=60),
            preserve_default=False,
        ),
    ]