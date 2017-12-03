# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models


class department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class professor(models.Model):
    user = models.OneToOneField(User)
    department = models.ForeignKey(department, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100)
    office = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    residence = models.CharField(max_length=100, default="")
    about_me = models.CharField(max_length=2000, default="")
    university = models.CharField(max_length=100, default="")
    pic = models.ImageField(upload_to='profile_image/', default='default.png')


    def get_absloute_url(self):
        return reverse('prof:my_profile', kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name


class publication_journals(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    published_at = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    co_authors = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class publication_conferences(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    published_at = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    co_authors = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class publication_books(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    published_at = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    co_authors = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class publication_thesis(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    published_at = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    co_authors = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class student_ongoing(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thesis_title = models.CharField(max_length=100)
    year_start = models.CharField(max_length=100)
    year_end = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class student_completed(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    thesis_title = models.CharField(max_length=100)
    year_start = models.CharField(max_length=100)
    year_end = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class award_achievement(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    awarded_by = models.CharField(max_length=100)
    awarded_at = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class award_fellowships(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    awarded_by = models.CharField(max_length=100)
    awarded_at = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class education(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.degree + ' ' + self.field + ' ' + self.university


class experience(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year_start = models.CharField(max_length=100)
    year_end = models.CharField(max_length=100)

    def __str__(self):
        return self.designation + ' ' + self.university


class project(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    PI = models.CharField(max_length=100)
    FA = models.CharField(max_length=100)
    year_start = models.CharField(max_length=100)
    year_end = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class course(models.Model):
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    year_start = models.CharField(max_length=100)
    year_end = models.CharField(max_length=100)

    def __str__(self):
        return self.code + ' ' + self.name