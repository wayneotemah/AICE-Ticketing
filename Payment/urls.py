from django.urls import path
from . import views


urlpatterns = [
    path('client',views.ClientViewSet.as_view({'get':'list','post':'create'})),
    path('pay',views.PaymentViewSet.as_view({'get':'list','post':'create'})),
]