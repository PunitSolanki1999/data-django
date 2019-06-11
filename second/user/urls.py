from django.urls import path
from .views import data_view,user_login,interface,logged,logout


app_name = 'user'
urlpatterns = [
    path('logout/',logout,name='logout'),
    path('',interface,name='interface'),
    path('logged/',logged,name='logged'),
    path('sign_up/',data_view,name= 'user-signup'),
    path('login/',user_login,name='user-login'),
]
