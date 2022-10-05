from django.urls import path
from .views import *

app_name = "reader"


urlpatterns = [
    path('register', RegisterApiView.as_view(), name="register"),
    path('load_data', LoadView, name="load_data")
]

