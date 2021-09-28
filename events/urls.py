from django.urls import path
from .views import SaveEvent

urlpatterns = [
    path('create', SaveEvent.as_view())
]