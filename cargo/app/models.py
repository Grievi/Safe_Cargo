from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=255)
    Id_No=models.IntegerField()
    address=models.CharField(max_length=20)
    mobile_no=models.IntegerField()

    def __str__(self):
        return self.user.username

class Cargo(models.Model):
    
    Duration=[
        ('30 days',30),
        ('60 days', 60),
        ('90 days',90),
        ('180 days',180),
        ('1yr-above', 365)
    ]
   
    Weight=[
        ('0-100kgs',1),
        ('101-500kgs',2) ,
        ('501-1000kgs',3),
        ('1000 and above',4)

    ]

    rf='refrigerated'
    el='electronics'
    mc='machinery'
    ol='other_luggage'

    Type=[
        (rf,'refrigerated'),
        (el, 'electronics'),
        (ol,'other_luggage'),
        (mc,'machinery')
    ]

    duration=models.CharField(max_length=20, choices=Duration, default='default')
    type_cargo=models.CharField(max_length=20, choices=Type, default='choose_type')
    weight_category=models.CharField(max_length=20, choices=Weight, default='weight')
    cargo=models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')

# class Prices(models.Model):

