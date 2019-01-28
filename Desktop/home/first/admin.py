# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Results

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
        pass


class ResultsAdmin(admin.ModelAdmin):
        pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Results, ResultsAdmin)

