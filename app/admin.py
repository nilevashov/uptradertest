from django.contrib import admin
from django.forms import ModelForm

from .models import Menu, MenuItem

# Register your models here.

class MenuItemForm(ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'title', 'url', 'parent']


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    form = MenuItemForm
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(Menu, MenuAdmin)