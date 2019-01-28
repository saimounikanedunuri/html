# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    hallticket_no = models.CharField(max_length=40)
    mail_id = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)


class Results(models.Model):
    hallticket_no = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    marks = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)


class Lecturer(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    subject = models.ForeignKey(Student, on_delete=models.CASCADE)
