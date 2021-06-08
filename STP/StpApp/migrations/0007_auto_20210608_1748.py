# Generated by Django 3.2.4 on 2021-06-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StpApp', '0006_auto_20210608_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudName', models.CharField(max_length=60)),
                ('StudAadhar', models.BigIntegerField()),
                ('R1Marks', models.IntegerField()),
                ('R2Marks', models.IntegerField()),
                ('R3Marks', models.IntegerField()),
                ('StudTotal', models.IntegerField()),
                ('R1File', models.FileField(blank=True, null=True, upload_to='Student_Review1_File')),
                ('R2File', models.FileField(blank=True, null=True, upload_to='Student_Review2_File')),
                ('R3File', models.FileField(blank=True, null=True, upload_to='Student_Review3_File')),
                ('StudCertificate', models.FileField(blank=True, null=True, upload_to='Student_Certificate')),
            ],
        ),
        migrations.AlterField(
            model_name='tupload',
            name='treview1',
            field=models.FileField(blank=True, default='', null=True, upload_to='treview1'),
        ),
        migrations.AlterField(
            model_name='tupload',
            name='treview2',
            field=models.FileField(blank=True, default='', null=True, upload_to='treview2'),
        ),
        migrations.AlterField(
            model_name='tupload',
            name='treview3',
            field=models.FileField(blank=True, default='', null=True, upload_to='treview3'),
        ),
    ]