# coding: utf-8

from models import News
from noema_site.utils import standard_view

from noema_site.context.context import get_context_list

current_menu = 'news'

@standard_view('news/news.html', current_menu)
def view_news(request):
    news_list = get_context_list(News.objects.all())
    current = current_menu
    is_super_user = request.user.is_superuser
    return locals()


def view_one_news(request, news_id):
    return {}