from django.urls import path,include
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('about/',views.about),
    path('contact/',views.contact),
    
]
