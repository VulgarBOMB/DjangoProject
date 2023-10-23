from django.contrib import admin
from .models import *


# class BbAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content', 'price', 'published', 'rubric')
#     list_display_links = ('title', 'content')
#     search_fields = ('title', 'content', 'price', 'published')


# class RubricAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_display_links = ('name',)
#     search_fields = ('name',)


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'calories',)
    list_display_links = ('name',)
    search_fields = ('name', 'weight', 'calories',)


class LunchAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',)
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'price',)


# admin.site.register(Bb, BbAdmin)
# admin.site.register(Rubric, RubricAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Lunch, LunchAdmin)
admin.site.register(LunchStructure)
