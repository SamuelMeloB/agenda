"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core import views, models
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>/', views.hello),
    path('eventos/<titulo_evento>/', views.eventos),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/',views.evento),
    path('agenda/evento/submit',views.submit_evento),
    path('', RedirectView.as_view(url = '/agenda/')), #ou colocar views.index e descomitar no views
    path('login/',views.login_user),
    path('login/submit', views.submit_login),
    path('agenda/logout/', views.logout_user)
]
