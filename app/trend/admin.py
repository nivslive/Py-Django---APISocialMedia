from django.contrib import admin
from .models import Trend

class TrendAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'event', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('context',)

admin.site.register(Trend, TrendAdmin)
