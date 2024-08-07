from rest_framework import serializers

from .models import Payment,Client

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name","email","phone_number","company","transaction_code"]
        extra_kwargs = {"user_id": {"read_only": True}}