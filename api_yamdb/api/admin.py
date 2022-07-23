from django.contrib import admin

from titles.models import Title, Category, Genre
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'username',
        'bio',
        'email',
        'role',
    )
    empty_value_display = '-empty-'


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'description', 'category']
    search_fields = ['name', 'year', 'description']
    list_filter = ['category', 'genre']
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Category)
admin.site.register(Genre)
