from django.db import models
from django.contrib import admin

# Create your models here.


class RegForm(models.Model):
    sno = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=60)
    dob = models.DateField()
    gender = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    aadhar = models.BigIntegerField()
    fname = models.CharField(max_length=60)
    foccupation = models.CharField(max_length=60)
    institutename = models.CharField(max_length=100)
    course = models.CharField(max_length=60)
    presentyear = models.CharField(max_length=60)
    percentage12 = models.CharField(max_length=60)
    cgpa = models.CharField(max_length=60)
    photograph = models.ImageField(upload_to='Photographs', default="")
    marksheet12 = models.FileField(upload_to='Marksheets_12', default="")
    lmarksheet = models.FileField(upload_to='Latest_Marksheets', default="")
    bletter = models.FileField(upload_to='Bonafied_Letters', default="")
    counter = models.IntegerField(default=0)

    def __str__(self):
        return "%s (%s)" % (self.aadhar, self.name)


class TUpload(models.Model):
    tusername = models.CharField(max_length=60)
    treview1 = models.FileField(
        upload_to='treview1', default="", blank=True, null=True)
    treview2 = models.FileField(
        upload_to='treview2', default="", blank=True, null=True)
    treview3 = models.FileField(
        upload_to='treview3', default="", blank=True, null=True)

    def __str__(self):
        return "%s" % (self.tusername)

    def delete(self, *args, **kwargs):
        self.treview1.delete()
        self.treview2.delete()
        self.treview3.delete()
        return super().delete(*args, **kwargs)


class StudData(models.Model):
    StudName = models.CharField(max_length=60)
    StudAadhar = models.BigIntegerField()
    R1Marks = models.IntegerField()
    R2Marks = models.IntegerField()
    R3Marks = models.IntegerField()
    StudTotal = models.IntegerField()
    R1File = models.FileField(
        upload_to='Student_Review1_File', blank=True, null=True)
    R2File = models.FileField(
        upload_to='Student_Review2_File', blank=True, null=True)
    R3File = models.FileField(
        upload_to='Student_Review3_File', blank=True, null=True)
    StudCertificate = models.FileField(
        upload_to='Student_Certificate', blank=True, null=True)

    def __str__(self):
        return "%s (%s)" % (self.StudAadhar, self.StudName)
