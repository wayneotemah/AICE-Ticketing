from django.db import models

#Name, Email, comapany, Mpesa code, date, amount, time. phone number


class Client(models.Model):
    user_id  = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Payment(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    Trasaction_code = models.CharField(unique=True,max_length=100)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name