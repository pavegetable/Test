from django.contrib import admin
from django.urls import path, include

from courses import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
]
