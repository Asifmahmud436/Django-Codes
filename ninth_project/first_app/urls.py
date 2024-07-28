from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.set_session),
    path('get/', views.get_cookie),
    path('session/', views.get_session),
    path('del/', views.delete_session),
]
