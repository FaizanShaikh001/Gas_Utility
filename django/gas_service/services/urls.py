from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
