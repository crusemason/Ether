from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView
from . import views
from uploads import views as upload_views
from .forms import UserLoginForm
from django.contrib.auth import views as a_views
from django.conf.urls import url


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', upload_views.mydrive),
    path('createaccount/',views.indexView),
    path('login/',a_views.LoginView.as_view(template_name="login.html",
            authentication_form=UserLoginForm),name='login'),
    path('loginpw/', views.user_login, name='loginpw'),
    #path('loginpw/',a_views.LoginView.as_view(template_name="loginpw.html",
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

]

