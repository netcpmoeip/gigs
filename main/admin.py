from django.contrib import admin
from .models import Page, News, Leg

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

class LegAdmin(admin.ModelAdmin):
    list_display = ('title', 'departure')


admin.site.register(Page, PageAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Leg, LegAdmin)