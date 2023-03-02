SLUG_ALLOWED = False

def get_item_tree(menu_items, request, is_first_call=True):
    menu_html = ''
    # В зависимости от ступени рекурсии присваиваем имя класса списку
    if is_first_call:
        menu_html += f'<ul class="menu_block">'
    else:
        menu_html += '<ul class="menu_block__item">'
    for menu_item in menu_items:
        if not menu_item.has_parent() or not is_first_call:
            menu_html += '<li>'
            # Если включен режим перехода по сгенерированным ссылкам
            if SLUG_ALLOWED:
                url = menu_item.slug
                print("URL:", url)
            # Иначе вставляем кастомные (из бд)
            else:
                url = menu_item.url
                print("URL:", url)
            if request.path in [menu_item.slug, menu_item.url]:
                menu_html += f'<a href="{url}" class="active">{menu_item.name}</a>'
            else:
                menu_html += f'<a href="{url}">{menu_item.name}</a>'
            if menu_item.has_children():
                menu_html += get_item_tree(menu_item.children.all(), request, is_first_call=False)
            menu_html += '</li>'
    menu_html += '</ul>'
    
    return menu_html