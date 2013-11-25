# -*- coding: utf-8 -*-
from django.contrib import admin
from magnet.models import Term, Magnet


class MagnetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'

admin.site.register(Magnet, MagnetAdmin)
admin.site.register(Term)
