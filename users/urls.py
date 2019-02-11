from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('signup/', views.signup, name='signup_page'),
    path('profile/', views.profile, name='profile_page'),
    # HERE WE OVERRIDED THE LOGIN/LOGOUT ROUTE HANDLING.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', extra_context={'title': 'Login'}), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html', extra_context={'title': 'Logout'}), name='logout_page'),
    # HERE WE OVERRIDED THE LOGIN/LOGOUT ROUTE HANDLING.
]