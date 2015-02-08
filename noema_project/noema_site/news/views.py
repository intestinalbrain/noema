# coding: utf-8

from models import News
from noema_site.menu.models import Menu
from noema_site.utils import view

from noema_site.context.context import get_context_list

@view('news/news.html')
def view_news(request):
    news_list = get_context_list(News.objects.all())
    menu_list = get_context_list(Menu.get_noema_menu_item_list())
    title = u'Новости'
    return locals()


def view_one_news(request, news_id):
    return {}