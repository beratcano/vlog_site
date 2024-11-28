from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import VlogPost, Categories
# Register your models here.
class VlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author","published_date","get_tags")
    list_filter = ("tags",)
    filter_horizontal = ("tags",)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = "Tags"

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(VlogPost, VlogPostAdmin)
admin.site.register(Categories, CategoriesAdmin)