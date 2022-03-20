from django.urls import path, include
from .import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.hoods, name='hoods'),
    path('account/', include('django.contrib.auth.urls')),
    path('new-hood/', views.create_hood, name='new-hood'),
]