from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)

# Customized ModelAdmin class for Post and Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
