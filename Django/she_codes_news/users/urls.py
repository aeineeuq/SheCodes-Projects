from django.urls import path
from .views import CreateAccountView
from .views import ProfileView
from django.conf.urls.static import static
from django.conf import settings

# app_name = 'users'
urlpatterns = [
	path('create-account/', CreateAccountView.as_view(), name='createAccount'),
	path('<int:pk>/', ProfileView.as_view(), name='profile'),
]