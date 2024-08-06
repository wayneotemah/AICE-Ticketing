from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import ClientSerializer,PaymentSerializer
from .models import Client,Payment
# Create your views here.

class ClientViewSet(viewsets.ViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def post(self,request):
        # serializer = ClientSerializer(data=request.data)
        if self.serializer.is_valid():
            self.serializer.save()
            return Response(self.serializer.data,status=status.HTTP_201_CREATED)
        return Response(self.serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def  get(self,request):
        clients = self.queryset.all()
        serializer = self.serializer_class(clients,many=True)
        return Response(serializer.data)
    
    
class PaymentViewSet(viewsets.ViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def post(self,request):
        # serializer = PaymentSerializer(data=request.data)
        if self.serializer.is_valid():
            self.serializer.save()
            return Response(self.serializer.data,status=status.HTTP_201_CREATED)
        return Response(self.serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def  get(self,request):
        payments = self.queryset.all()
        serializer = self.serializer_class(payments,many=True)
        return Response(serializer.data)
    
    def  get(self,request,pk):
        payment = self.queryset.get(pk=pk)
        serializer = self.serializer_class(payment)
        return Response(serializer.data)
    
    def  put(self,request,pk):
        payment = self.queryset.get(pk=pk)
        serializer = self.serializer_class(payment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def  delete(self,request,pk):
        payment = self.queryset.get(pk=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)