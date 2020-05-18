#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence 
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: urls.py
@time: ??
"""
from django.urls import path
from . import views

app_name = "owntracks"

urlpatterns = [
    path('owntracks/logtracks', views.manage_owntrack_log, name='logtracks'),
    path('owntracks/show_maps', views.show_maps, name='show_maps'),
    path('owntracks/get_datas', views.get_datas, name='get_datas'),
    path('owntracks/show_dates', views.show_log_dates, name='show_dates')
]
