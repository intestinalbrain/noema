from django.shortcuts import render_to_response

from models import News
from noema_project.noema_site.menu.models import MenuItem

def get_context_list(obj_list):
    return [obj.context() for obj in obj_list]

@render_to_response('news/news.html')
def view_news(request):
    news_list = get_context_list(News.objects.all())
    menu_list = get_context_list(MenuItem.get_noema_menu_list())
    return locals()


def view_one_news(request):
    pass