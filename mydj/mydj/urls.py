from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index, name="home"),
    path('student/', include('main.urls')),
    path('teacher/', include('teacher.urls'))
]
