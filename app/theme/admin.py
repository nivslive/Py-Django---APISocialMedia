from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Theme

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)

admin.site.register(Theme, ThemeAdmin)
