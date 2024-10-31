from django.db import migrations, models

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    gender = models.CharField(blank=False, choices=gender_choices, max_length=10, default="M")
    dateofbirth=models.CharField(max_length=20,blank=False)
    salary=models.PositiveIntegerField(blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    def str(self):
        return self.fullname

    class Meta:
        db_table = "customer_table"





class Pawnbroker(models.Model):
    id=models.AutoField(primary_key=True)
    category_choices = (("Home", "Home"), ("Jewelry", "Jewelry"), ("Electronics", "Electronics"), ("Clothes","Clothers"),("Others","Others"))
    category = models.CharField(max_length=100, blank=False,choices=category_choices)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=200,blank=False)
    price = models.PositiveIntegerField(blank=False)
    image = models.FileField(blank=False,upload_to="productimages")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pawnbroker_table"


class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=50,blank=False)

    def str(self):
        return self.username

    class Meta:
        db_table = "admin_table"
