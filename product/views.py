from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AddProduct,Brand,Category,Warranty,Unit,SubCategory
from .serializers import AddProduct_Serializer,Brand_Serializer,Category_Serializer,Warranty_Serializer,Unit_Serializer,SubCategory_Serializer
from rest_framework import status

class BaseAPIView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        objects = self.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": f"New {self.model.__name__} Added!"}, status=status.HTTP_201_CREATED)
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        name = request.data.get('name')
        obj = self.model.objects.filter(name=name)
        if obj.exists():
            obj.delete()
            return Response({"Message": f"Successfully deleted!"})
        return Response({"Error": f"{self.model.__name__} not found."})

class Brand_Api(BaseAPIView):
    model = Brand
    serializer_class = Brand_Serializer

class Category_Api(BaseAPIView):
    model = Category
    serializer_class = Category_Serializer

class SubCategory_Api(BaseAPIView):
    model = SubCategory
    serializer_class = SubCategory_Serializer

class Warranty_Api(BaseAPIView):
    model = Warranty
    serializer_class = Warranty_Serializer

class Unit_Api(BaseAPIView):
    model = Unit
    serializer_class = Unit_Serializer

class AddProduct_Api(BaseAPIView):
    model = AddProduct
    serializer_class = AddProduct_Serializer







