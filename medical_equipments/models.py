from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError



# Create your models here.
#auto_now_add=True


groups = [
	("operating-theatre-equipment","Operating Theatre Equipment"),
    ("ob-gyn-equipment","OB/GYN Equipment"),  
    ("diagnostic-equipment","Diagnostic Equipment"),
    ("sterilizer-autoclave","Sterilizer (Autoclave)"),
    ("laboratory-equipment","Laboratory Equipment"),
    ("x-ray-series","X-ray Series"),
    ("in-vitro-diagnostics","In-Vitro Diagnostics"),
    ("hospital-furniture","Hospital Furniture"),
    ("walking-aids","Walking Aids"),
    ("first-aid-products","First-Aid Products"),
    ("ophthalmic-equipment","Ophthalmic Equipment"),
    ("dental-equipment","Dental Equipment"),
    ("ent-equipment","ENT Equipment"),
    ("home-care-equipment","Home Care Equipment"),
    ("veterinary-equipment","Veterinary Equipment"),
    ("medical-consumables","Medical Consumables"),
	

]


class shop(models.Model):
    image =models.ImageField(upload_to='shopImages',help_text="width:270px,heigth:350px")
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=120, choices= groups)
    description = models.TextField()
    slug = models.SlugField(max_length=150,unique=True)
    price = models.IntegerField(default=0)
    datepost = models.DateTimeField(default=datetime.now, blank=True)
    publish = models.BooleanField(default=True)
   


    class Meta:
        ordering = ['-datepost']

    def __str__(self):
        return self.name

    def clean(self):
        if not self.image:
            raise ValidationError("No image selected!")
        else:
            w,h = get_image_dimensions(self.image)
            if w != 270 and h != 350 :
                raise ValidationError("The image dimensions expected is width =270px and height=350px")
            else:
                return self.image

    

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
