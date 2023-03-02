from django import template
from django.utils.safestring import mark_safe

from ..tools.get_menu_items import get_item_tree
from ..models import Menu, MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    try:
        # Получаем из бд сразу же все дерево меню
        menu = Menu.objects.prefetch_related("items__children").get(name=menu_name)
        menu_items = menu.items.all()
    except Menu.DoesNotExist:
        return ''
    menu_html = get_item_tree(menu_items, request)
    return mark_safe(menu_html)
