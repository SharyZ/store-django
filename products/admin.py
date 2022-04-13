from django.contrib import admin
from django.utils.html import format_html

from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="80" style="border-radius: 50%;" />'.format(object.image.url))

    thumbnail.short_description = 'Product image'

    list_display = ('id', 'thumbnail', 'name',
                    'price', 'category', 'created_at')
    list_display_links = ('thumbnail', 'name')
    list_editable = ('price', 'category',)
    search_fields = ('name', 'small_description',)
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
