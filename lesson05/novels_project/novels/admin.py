from django.contrib import admin

from novels.models import Author, Novel

class NovelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "original_title", "description", "author")
    list_filter = ("author",)

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "bio", "country")
    list_filter = ("country",)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
    
admin.site.register(Novel, NovelAdmin)
admin.site.register(Author, AuthorAdmin)