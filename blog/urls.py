from . import views
from django.urls import  path

app_name = "blog"
urlpatterns = [
    path('', views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('verify/',views.verify,name="verify"),
]
