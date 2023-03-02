from django.shortcuts import render

# Create your views here.

def get_main_page(request, menu="", title="", path=''):
    return render(request, 'base.html', context={'title': title, 'menu_name': menu, 'path': path})
