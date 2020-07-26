from django.db import models

# Create your models here.
class category(models.Model):
    c_id = models.AutoField(primary_key=True) 
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class product(models.Model):
    p_id = models.AutoField(primary_key=True) 
    price = models.IntegerField(default=0)
    p_name = models.CharField(max_length=50)
    Size = models.CharField(max_length=50, default='', null=True)
    Models = models.CharField(max_length=50, default='',null=True)
    desc = models.TextField() 
    image = models.ImageField(upload_to="images", default="")
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=100) 
   
    pub_date = models.DateField()
   
    def __str__(self):
        return self.p_name

class customer(models.Model):
    c_id = models.AutoField(primary_key=True) 
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100) 
    password = models.CharField(max_length=200)
   
    def __str__(self):
        return self.f_name