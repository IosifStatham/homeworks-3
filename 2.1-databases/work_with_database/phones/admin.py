from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    slug = {"slug": ["name"]}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
