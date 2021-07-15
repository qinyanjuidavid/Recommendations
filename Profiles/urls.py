from django.urls import path

from Profiles import views

app_name = "Profiles"

urlpatterns = [
    path('', views.mainView, name="main"),
    path('<ref_code>/', views.mainView, name="main"),
]
