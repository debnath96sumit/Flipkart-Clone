from django.db import models

# Create your models here.
class userdata(models.Model):
    number = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=50, null=True)
    firstname = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.firstname


class product(models.Model):
    name= models.CharField(max_length=50, null=True)
    price= models.IntegerField(default=0)
    catagory= models.CharField(max_length=50, null=True)
    desc = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to="home/images", default="")

    def __str__(self):
        return self.name

class contact(models.Model):
    email = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    desc = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name