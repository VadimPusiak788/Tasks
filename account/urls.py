from django.urls import path
from .views import RegisterView, LogoutView
from django.contrib.auth import views as auth_views

app_name = 'account'


urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login')
]