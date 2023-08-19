from django.contrib import admin
from .models import Blog,Category,TopWeek
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug","category",)
    search_fields = ("title",)
    list_filter = ("is_active","is_home","categories",)

    def category(self,obj):
        html = ""
        for c in obj.categories.all():
            html += c.name + " | "
        return html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
    search_fields = ("name",)

class TopWeekAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","last_week","slug",)
    search_fields = ("title",)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(TopWeek,TopWeekAdmin)