'''
Created on Jun 8, 2015

@author: pta
'''

from django.conf.urls import url

from . import views
from quiz.views import CathiDetailView, DethiStartView, CaThiTuLuanView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login_user'),
    
    url(r'^cathi/(?P<pk>[\d]+)/$', CathiDetailView.as_view(), name="cathi_detail"),
    url(r'^cathi/(?P<pk>[\d]+)/start/$', DethiStartView.as_view(), name='dethi_start'),
    url(r'^cathi/(?P<pk>[\d]+)/start/finish/$', views.quiz_finish, name='quiz_finish'),
    url(r'^tuluan/preview/(?P<pk>[\d]+)/$', views.view_pdf, name='view_pdf'),
    url(r'^tuluan/preview/dethi/(?P<pk>[\d]+)/$', views.view_dethi, name='view_dethi'),
    url(r'^tuluan/preview/dapan/(?P<pk>[\d]+)/$', views.view_dapan, name='view_dapan'),
    
    url(r'^tuluan/get_dt/(?P<pk>[\d]+)/$', CaThiTuLuanView.as_view(), name='get_dt'),
    url(r'^tuluan/get_dt/(?P<pk>[\d]+)/sinhde/$', views.sinh_de, name='sinhde'),
    
]