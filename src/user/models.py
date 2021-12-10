from django import forms
from django.db import models
from django.db.models.deletion import CASCADE
from twilio.rest import Client

# Create your models here.

account_sid = 'AC4474e42eb226a7a0a8e9133a8b17a82c' 
auth_token = '943417ead37eb6dc21a6160ac11ac830' 
client = Client(account_sid, auth_token) 

class Client(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self) -> str:
        return self.name + ' ' + self.lastName


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField()
    message_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.client.name + ' ' + str(self.date)

    def save(self, *args, **kwargs) -> None:
        print(self.client)
        message = client.messages.create( 
            from_='whatsapp:+14155238886',  
            body=f'Your appointment is coming up on {self.date} at {self.time}',      
            to='whatsapp:' + self.client.phone
        )
        self.message_id = message.sid
        return super().save(*args, **kwargs)