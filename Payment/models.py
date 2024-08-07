from django.db import models

#Name, Email, comapany, Mpesa code, date, amount, time. phone number


class Client(models.Model):
    user_id  = models.AutoField(primary_key=True)   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    transaction_code = models.CharField(unique=True,max_length=100)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"


class Payment(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    transaction_code = models.CharField(unique=True,max_length=100)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.client}"