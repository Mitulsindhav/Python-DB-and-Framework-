from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name='index'),
    # path('admin/', admin.site.urls),
    path('', views.register, name='register'),
]
