from django.urls import path

from Profiles import views

app_name = "Profiles"

urlpatterns = [
    path('home/', views.mainView, name="main"),
    path('home/<ref_code>/', views.mainView, name="main"),
    path('', views.SignupView, name="signUp"),
]
