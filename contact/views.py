from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Suppliers,Customers
from .serializers import Suppliers_Serializer,Customers_Serializer
from .models import Action

class Suppliers_Api(APIView):
    def post(self,request):
        serializer=Suppliers_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"Message":"Suppliers record Created!"})
        return Response({"Error":"Error! Check correctly"})
    
    def delete(slef,request):
        contact_id=request.data['contact_id']
        serializer=Suppliers.objects.filter(contact_id=contact_id)
        serializer.delete
        return Response({"Message":"Successfully deleted!"})
        
    



class Customers_Api(APIView):
    def post(self,request):
        serializer=Customers_Serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()

            return Response({"Message":"Customers record Created!"})
        return Response({"Error":"Error! Check correctly"})
    
    def delete(slef,request):
        contact_id=request.data['contact_id']
        serializer=Customers.objects.filter(contact_id=contact_id)
        serializer.delete
        return Response({"Message":"Successfully deleted!"})

class Action_Api(APIView):
    def post(slef,request):
        action=request.data['action']

        
            