from django.urls import path
from .views import LoginUserView, RegisterUserView, LoginUserSerializer

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view())
]