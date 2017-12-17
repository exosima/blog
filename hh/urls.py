from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.index),
    path('get/posts/<int:hh>',views.get_post)
]
