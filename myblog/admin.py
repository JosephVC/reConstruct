from django.contrib import admin
from myblog.models import Post, Category
from django.core import urlresolvers
from django.utils.html import format_html
from django.utils import timezone

# Register your models here.

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

def bulk_publish(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())

class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'link_to_author', 'created_date',
                    'modified_date', 'published_date')
    inlines = [
        CategoryInline,
    ]

    actions = [bulk_publish]

    readonly_fields = (
        'created_date', 'modified_date',
        )

    def link_to_author(self, obj):
        author_url = urlresolvers.reverse('admin:auth_user_change', args=(obj.author.id,))
        html = format_html('<a href="{}">{}</a>', author_url, obj.author)
        return html
    link_to_author.short_description = 'Author'

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)