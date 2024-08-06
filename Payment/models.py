from django.db import models

#Name, Email, comapany, Mpesa code, date, amount, time. phone number

class Payment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    Trasaction_code = models.CharField(unique=True,max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name