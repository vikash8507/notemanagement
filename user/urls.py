
from django.urls import path
from user.views import home, RegisterView

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
]
