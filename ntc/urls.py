"""ntc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_views
from examenes import views as examenes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/login/',users_views.login_view,name='login'),
    path('users/signup/',users_views.signup ,name='signup'),
    path('users/editar_usuario/<int:pk>/',users_views.editar_usuario ,name='editar_usuario'),

    path('menu/', examenes_views.inicio,name='home'),
    path('enviar/', examenes_views.send_email,name='enviar'),
]
