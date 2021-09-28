from rest_framework.views import APIView

from .models import Event

# Create your views here.


class SaveEvent(APIView):

    def post(self, request):
        data = request.data
        Event.objects.create(**data)

