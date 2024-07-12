from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)

# Customized ModelAdmin class for Post and Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
