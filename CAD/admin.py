from django.contrib import admin
from .models import Article
from .models import Person

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
# Register your models here.
