from django.contrib import admin

# Register your models here.

from .models import Questions, Choice


class ChoiceTabularInline(admin.TabularInline):
    model = Choice
    extra = 0

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceTabularInline]
