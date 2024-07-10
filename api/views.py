from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockDataSerializer
from core.models import StockData

class StockDataAPIView(APIView):
    def get(self, request):
        stocks = StockData.objects.all()
        serializer = StockDataSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StockDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
