from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/<str:username>/', views.dashboard, name='dashboard'),
    path('reg',views.reg,name="registeration"),
    path('logout/', LogoutView.as_view(), name='logout'),
]