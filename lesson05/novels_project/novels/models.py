from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

def validate_positive(value):
    if value < 0:
        raise ValidationError(gettext_lazy("%d < 0" % value))

class Author(models.Model):
    name = models.CharField(max_length=128, null= True, blank=True, verbose_name="Имя")
    bio = models.TextField(null= True, blank=True, verbose_name="О себе")
    country = models.CharField(max_length=64, blank=True, null=True, verbose_name="Страна")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ("name", "bio", "country")

    def __str__(self):
        return self.name

class Novel(models.Model):
    title = models.CharField(max_length=128, help_text="Название новеллы",
            null=True, blank=True, verbose_name="Название")
    original_title = models.CharField(max_length=128, blank=True, 
            null=True, help_text="Оригинальное название новеллы", verbose_name="Оригинальное название")
    description = models.TextField(blank=True, null=True, 
            help_text="Описание", verbose_name="Описание")
    
    author = models.OneToOneField(Author, on_delete=models.CASCADE, null=True,
            blank=True, verbose_name="Автор")

    class Meta:
        verbose_name = "Новелла"
        verbose_name_plural = "Новеллы"
        ordering = ("title", "description", "author", "original_title")
    
    def __str__(self):
        return ( 
            self.title
            + (" [" + self.original_title + "], " if self.original_title else "")
            + (self.description if self.description else "")
        )
        