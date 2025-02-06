from django.urls import path, include
from rest_framework import routers
from complaint import views

router = routers.DefaultRouter()
router.register(r'', views.ComplaintView, 'complaints')

urlpatterns = [
    path("api/", include(router.urls)),
]