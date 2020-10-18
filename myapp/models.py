from django.db import models

# Create your models here.
class DetailsOfEvent(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
choices=(
    ("Organise","organise"),
    ("Attend","Attend"),
    ("Sponsor","Sponsor"),
)
class UserCreation(models.Model):
    name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=15,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=100,null=True)
    position=models.CharField(max_length=100,choices=choices)
    otp=models.CharField(max_length=7,null=True)

    def __str__(self):
        return self.name
class Attend(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Sponsor(models.Model):
    name=models.CharField(max_length=100,null=True)
    Amount =models.IntegerField()
    def __str__(self):
        return self.name