from django.conf.urls import url
from auth.auth_app import views

 #TEMPLATE URLS

app_name = 'auth_app'

urlpatterns = [
    url(r"^register/$", views.register, name='register'),
    url(r'user_login/$', views.user_login, name='user_login'),
]