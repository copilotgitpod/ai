from rest_framework.views import APIView
from rest_framework.response import Response
import random

class RandomNewsView(APIView):
    def get(self, request):
        news = [
            {"title": "News 1", "content": "Content 1"},
            {"title": "News 2", "content": "Content 2"},
            {"title": "News 3", "content": "Content 3"},
            # Add more news here
        ]
        return Response(random.choice(news))
