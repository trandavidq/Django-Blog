from . import views
from django.urls import  path

app_name = "blog"
urlpatterns = [
    path('', views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('verify/',views.verify,name="verify"),
    path('logout/',views.logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('post',views.post,name="post"),
    path('delete',views.delete,name="delete"),
]
