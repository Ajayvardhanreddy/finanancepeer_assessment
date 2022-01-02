from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('upload_json/', views.upload_json, name='upload_json'),
    path('get_json_data/', views.get_json_data, name='get_json_data'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]
