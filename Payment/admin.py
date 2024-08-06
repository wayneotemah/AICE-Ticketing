from django.contrib import admin
from .models import Payment,Client



class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number','company']
    search_fields = ['name','email','phone_number','company']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['client','Trasaction_code','date','time']
    search_fields = ['Trasaction_code','date','time']
    list_filter = ['date','time']
    

admin.site.register(Payment,PaymentAdmin)
admin.site.register(Client,ClientAdmin)

