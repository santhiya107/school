from django.urls import path
from .views import (
    SignupView,
    LoginView,
    StudentProfileView,
    UserDetailsView,
    StudentProfileView,
    UserDetailsView,
    UserDetailsEditView,
    LogoutView,
    LoginVerifyView,
    SimpleLoginView,
    ProfileView,
)
from django.views.decorators.csrf import csrf_exempt




urlpatterns=[
    path('signup/',csrf_exempt(SignupView.as_view())),
    path('login/',LoginView.as_view()),
    path('login-verify/',LoginVerifyView.as_view()),
    path('simple-login/',csrf_exempt(SimpleLoginView.as_view())),
    path('logout/',LogoutView.as_view()),
    path('student-profile/<int:pk>/',StudentProfileView.as_view()),
    path('user-details/',UserDetailsView.as_view()),
    path('user-details/<int:pk>/',UserDetailsEditView.as_view()),
    path('profile/',ProfileView.as_view()),
]