from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('other/',views.other,name='other'),
    path('login',views.user_login,name='user_login')
]
