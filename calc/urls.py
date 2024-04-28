from django.urls import path
from . import views
from .views import FingerprintView, add_fingerprint


urlpatterns = [
    path('fingerprint/', FingerprintView.as_view(), name='fingerprint'),
    path('add_fingerprint/', add_fingerprint, name='add_fingerprint'),
]
