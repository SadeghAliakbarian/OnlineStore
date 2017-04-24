from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/$', views.products, name='products'),
    url(r'^dealers/$', views.dealers, name='dealers'),
    url(r'^dealer_detail/(?P<dealer_id>[0-9]+)$', views.dealer_detail, name='dealer_detail'),
    url(r'^product_detail/(?P<product_id>[0-9]+)$', views.product_detail, name='product_detail'),

]