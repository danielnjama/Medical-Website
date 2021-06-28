from django.shortcuts import render,get_object_or_404
from datetime import datetime
from . models import shop
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from datetime import datetime
from django.db.models  import Q
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import time
#views for tarragon medics starts here
def index(request):
    today = datetime. now()
    items = shop.objects.all()
    return render(request,"medical/index.html",{"today":today,"items":items})

def aboutus(request):
    today = datetime. now()
    return render(request,"medical/about.html",{"today":today})

def contactus(request):
    message = ""
    today = datetime.now()
    if request.method == "POST":
        name = request.POST.get('name')
        from_email = request.POST.get('email',)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        message = 'Name: {} \nEmail: {}\n{}'.format(name,from_email,message)
        recipient = settings.EMAIL_HOST_USER
        if subject != "" and message != "" and from_email != recipient:
            #send_mail(subject=subject,message=message,from_email=from_email ,recipient_list=[recipient,],fail_silently=False)
            emailing=EmailMessage(subject=subject,body=message,from_email=request.POST.get('email',) ,to=[recipient,])
            emailing.send()
            message='Your message has been sent. Thank you for choosing Tarragon Medics\nYour only trusted Medical equipment suppliers'
            return render(request,"medical/message.html",{"today":today,"message":message})
    return render(request,"medical/contact-us.html",{"today":today,"message":message})



def operating_theatre_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="operating-theatre-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def ob_gyn_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="ob-gyn-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})

def diagnostic_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="diagnostic-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def sterilizer(request):
    today = datetime. now()
    items = shop.objects.filter(category="sterilizer-autoclave")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def laboratory_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="laboratory-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def xray_series(request):
    today = datetime. now()
    items = shop.objects.filter(category="x-ray-series")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def invitro_diagnostics(request):
    today = datetime. now()
    items = shop.objects.filter(category="in-vitro-diagnostics")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def hospital_furniture(request):
    today = datetime. now()
    items = shop.objects.filter(category="hospital-furniture")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def walking_aids(request):
    today = datetime. now()
    items = shop.objects.filter(category="walking-aids")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def firstaid_products(request):
    today = datetime. now()
    items = shop.objects.filter(category="first-aid-products")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def ophthalmic_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="ophthalmic-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def dental_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="dental-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def ent_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="ent-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def home_care_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Home_Care_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def veterinary_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="veterinary-equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def medical_consumables(request):
    today = datetime. now()
    items = shop.objects.filter(category="medical-consumables")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})

def store(request):
    today = datetime.now()
    items = shop.objects.all()
    instagram = items
    keyws =[]
    for i in items:
        keyws.append(i.name)
    keywords = list(keyws)
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram,"keywords":keywords})
    
    



def shop_details(request,slug,category):
    today = datetime. now()
    item = get_object_or_404(shop,slug=slug)
    items = shop.objects.exclude(id=item.id)
    category = item.category
    whatsapp_message = "Hi, Im interested with the product posted on your website: " + item.name
    message = whatsapp_message.replace(" ","%20")
    return render(request,"medical/shop-detail.html",{"item":item,"items":items,"today":today,"message":message})


def search(request):
    today = datetime. now()
    item_instance = request.GET.get('q')
    items = shop.objects.filter(
        Q(name__contains=item_instance) or Q(description__contains=item_instance)
        )

    return render(request,"medical/search.html",{"items":items,"today":today})