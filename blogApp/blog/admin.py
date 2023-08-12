from django.contrib import admin
from .models import Blog,Category,TopWeek
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home",)
    search_fields = ("title",)

class TopWeekAdmin(admin.ModelAdmin):
    list_display = ("title","is_home","slug",)
    search_fields = ("title",)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(TopWeek,TopWeekAdmin)