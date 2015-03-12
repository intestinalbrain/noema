# coding: utf-8

from noema_site.news.models import News
from noema_site.menu.models import Menu
from noema_site.utils import view

from noema_site.context.context import get_context_list

current_menu = 'gallery'

@view('news/news.html')
def view_gallery(request):
    news_list = get_context_list(News.objects.all())
    menu_list = get_context_list(Menu.get_menu_item_list('noema'))
    submenu_list = get_context_list(Menu.get_submenu_item_list('noema', current_menu))
    title = u'Галлерея'
    is_super_user = request.user.is_superuser
    return locals()