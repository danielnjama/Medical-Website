from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.
#auto_now_add=True


groups = [
	("operating_theatre_equipment","Operating Theatre Equipment"),
    ("OB/GYN_equipment","OB/GYN Equipment"),  
    ("Diagnostic_Equipment","Diagnostic Equipment"),
    ("Sterilizer_(Autoclave)","Sterilizer (Autoclave)"),
    ("Laboratory_Equipment","Laboratory Equipment"),
    ("X-ray_Series","X-ray Series"),
    ("In-Vitro_Diagnostics","In-Vitro Diagnostics"),
    ("Hospital_Furniture","Hospital Furniture"),
    ("Walking_Aids","Walking Aids"),
    ("First-Aid_Products","First-Aid Products"),
    ("Ophthalmic_Equipment","Ophthalmic Equipment"),
    ("Dental_Equipment","Dental Equipment"),
    ("ENT_Equipment","ENT Equipment"),
    ("Home_Care_Equipment","Home Care Equipment"),
    ("Veterinary_Equipment","Veterinary Equipment"),
    ("Medical_Consumables","Medical Consumables"),
	

]


class shop(models.Model):
    image =models.ImageField(upload_to='shopImages',help_text="width:270px,heigth:350px")
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=120, choices= groups)
    description = models.TextField()
    slug = models.SlugField(max_length=150,unique=True)
    price = models.IntegerField()
    datepost = models.DateTimeField(default=datetime.now, blank=True)
    publish = models.BooleanField(default=True)
    
    
    


    class Meta:
        ordering = ['-datepost']

    def __str__(self):
        return self.name



    

    def save(self, *args, **kwargs):
        value = (self.name)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class reviews(models.Model):
    shops=  models.ForeignKey(shop,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
