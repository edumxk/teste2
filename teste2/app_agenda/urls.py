from django.urls import path
from . import views, urls

urlpatterns = [
    path ('', views.HomePageView.as_view(), name='home'),
]