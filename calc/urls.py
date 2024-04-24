from django.urls import path
from . import views
from .views import FingerprintView


urlpatterns = [
    path('fingerprint/', FingerprintView.as_view(), name='fingerprint'),
]
