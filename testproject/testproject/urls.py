from django.contrib import admin
from django.urls import path,include
from testapp import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('testapp.urls', namespace='testapp')),
    # path('auth/', include('django.contrib.auth.urls')),
    # path('/', views.home, name="home"),
]
