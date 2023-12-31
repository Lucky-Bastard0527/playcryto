from django.urls import path, include

from . import views

app_name = 'playcrypto'

urlpatterns = [
    path('', views.main, name='main'),
    path('charts', views.charts, name='charts'),
    path('layout_sidenav_light', views.layout_sidenav_light, name='layout_sidenav_light'),
    path('layout_static', views.layout_static, name='layout_static'),
    path('tables', views.tables, name='tables'),
    path('trading_bot/', views.trading_bot_view, name='trading_bot'),
]
