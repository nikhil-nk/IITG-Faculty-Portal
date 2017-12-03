# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import professor,department,education,award_fellowships,award_achievement,experience,project,publication_books,publication_conferences,publication_journals,publication_thesis,student_completed,student_ongoing
from django.contrib import admin

admin.site.register(professor)
admin.site.register(student_ongoing)
admin.site.register(student_completed)
admin.site.register(education)
admin.site.register(experience)
admin.site.register(department)
admin.site.register(award_achievement)
admin.site.register(award_fellowships)
admin.site.register(publication_thesis)
admin.site.register(publication_conferences)
admin.site.register(publication_books)
admin.site.register(project)
admin.site.register(publication_journals)
