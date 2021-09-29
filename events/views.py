from rest_framework.views import APIView
from rest_framework import serializers
from django.http import HttpResponse
from .models import Event
from .utils import get_request
import json


class EvensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SaveEvent(APIView):

    def post(self, request):
        data = request.data
        Event.objects.create(**data)
        return HttpResponse("Event saved", 400)


class ListEvents(APIView):

    def get(self, request):
        data = request.data

        # check if keys exits in request
        session_id = data.pop('session_id', None)
        category = data.pop('category', None)
        since = data.pop('since', None)
        until = data.pop('until', None)

        # validate if at least 1 exist
        if not(session_id or category or (since and until)):
            if since or until:
                response = f'Time range must be completed, it missed' \
                           f' {"until" if since else "since"}'
            else:
                response = 'Select an session_id, category or time range'
            return HttpResponse(response, 400)

        # create a query for the ORM
        params = get_request(session_id, category, since, until)

        # filter events
        events = Event.objects.filter(**params).values()

        return HttpResponse(json.dumps(list(events), indent=4, sort_keys=True, default=str))


