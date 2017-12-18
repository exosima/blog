from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get/posts/<int:hh>',views.get_post),
    path("get/po/<int:hh>",views.render_po),
]
