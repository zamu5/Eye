from django.urls import path
from .views import SaveEvent, ListEvents

urlpatterns = [
    path('create', SaveEvent.as_view()),
    path('list', ListEvents.as_view()),
]