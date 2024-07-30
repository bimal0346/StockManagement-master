from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Inventory,User_stock,All_Stock,Individual_Stock
from .serializers import All_Stock_serializer,User_Stock_serailizer,Inventory_serializer,Individual_Stock_serializer


# Create your views here.
class All_StockViewSet(viewsets.ViewSet):
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        qs = All_Stock.objects.all()
        serializer = All_Stock_serializer(qs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = All_Stock_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "New Item Created!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        qs = All_Stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer =  All_Stock_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        qs = All_Stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = All_Stock_serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Item Updated!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        qs = All_Stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = All_Stock_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Cart Partially Updated!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class User_Stock_Set(viewsets.ViewSet):
#    permission_classes = (IsAuthenticated,)

    def list(self, request):
        qs = User_stock.objects.all()
        serializer = User_Stock_serailizer(qs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = User_Stock_serailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "New Item Created!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        qs =User_stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = User_Stock_serailizer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        qs = User_stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = User_Stock_serailizer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Item Updated!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Individual_StockSet(viewsets.ViewSet):
#    permission_classes = (IsAuthenticated,)

    def list(self, request):
        qs = Individual_Stock.objects.all()
        serializer = Individual_Stock_serializer(qs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Individual_Stock_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "New Item Created!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        qs =Individual_Stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = Individual_Stock_serializer(item)
        return Response(serializer.data)

    def update(self, request, pk):
        qs = Individual_Stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = Individual_Stock_serializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Item Updated!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        qs = Individual_Stock.objects.all()
        item = get_object_or_404(qs, pk=pk)
        serializer = Individual_Stock_serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Cart Partially Updated!"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)






