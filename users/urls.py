from django.urls import path
from .views import home, profile, RegisterView,about
urlpatterns = [
    path('', home, name='users-home'),
    path('about/', about, name='users-about'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    ]
