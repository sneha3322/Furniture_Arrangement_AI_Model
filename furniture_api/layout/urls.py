from django.urls import path
from .views import predict_furniture

urlpatterns = [
    path("predict/", predict_furniture, name="predict_furniture"),
]