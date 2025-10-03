# Register your models here.
from django.contrib import admin
from .models import (Language, Branch, Semester, Subject, Unit, 
                    Note, PreviousPaper, Profile)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit', 'language')  
    list_filter = ('language', 'unit__subject__branch', 'unit__subject__semester')
    search_fields = ('title', 'unit__subject__name')


class PreviousPaperAdmin(admin.ModelAdmin):
    list_display = ('year', 'subject', 'uploaded_at')
    list_filter = ('year', 'subject__branch', 'subject__semester')
    search_fields = ('subject__name',)

admin.site.register(Language)
admin.site.register(Branch)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Unit)
admin.site.register(Note, NoteAdmin)
admin.site.register(PreviousPaper, PreviousPaperAdmin)
admin.site.register(Profile)
