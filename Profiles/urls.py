from django.urls import path

from Profiles import views

app_name = "Profiles"

urlpatterns = [
    path('', views.main_view, name="main"),
    path('<ref_code>/', views.main_view, name="main"),
]
