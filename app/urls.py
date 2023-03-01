from django.urls import path
from .views import UserCreate, WorkApiView

urlpatterns = [
    path("register/", UserCreate.as_view()),
    path("works", WorkApiView.as_view()),
]
