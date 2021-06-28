from django.shortcuts import render,get_object_or_404
from datetime import datetime
from . models import shop
from gates.models import items
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from datetime import datetime
from django.db.models  import Q

from gates.models import items
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from datetime import datetime
from django.db.models  import Q

# Create your views here.

#views for tarragon gates
##break
##break

def home(request):
    today = datetime. now()
    allitems=items.objects.filter(types__contains='gates')
    gates = items.objects.all()
    return render(request,'gates/index-home.html',{'allitems':allitems,'today':today,"gates":gates})

def contact(request):
    today = datetime. now()
    return render(request,'gates/contacts.html',{'today':today})

def swinging_gates(request):
    today = datetime. now()
    gates = items.objects.filter(types='swinging gates')
    types= "Swinging Gates"
    title = "Swinging Gates"
    return render(request,'gates/gates.html',{"today":today,"gates":gates,"types":types,"title":title})

def garage_gates(request):
    today = datetime. now()
    gates = items.objects.filter(types='garage gates')
    types= "Garage Gates"
    title = "Garage gates"
    return render(request,'gates/gates.html',{"today":today,"gates":gates,"types":types,"title":title})

def sliding_gates(request):
    today = datetime. now()
    gates = items.objects.filter(types='sliding gates')
    types= "Sliding Gates"
    title = "Sliding Gates"
    return render(request,'gates/gates.html',{"today":today,"gates":gates,"types":types,"title":title})



def about_us(request):
    today = datetime. now()
    allitems=items.objects.filter(types__contains='gates')
    return render(request,'gates/index.html',{'today':today,"allitems":allitems})



def cctv(request):
    today = datetime. now()
    gates = items.objects.filter(Q(types='Flood Lights') | Q(types="CCTV"))
    types="CCTV and Flood Lights"
    title = "CCTV and Flood Lights"
    return render(request,'gates/gates.html',{"today":today,"gates":gates,"types":types,"title":title})

def gallery(request):
    today = datetime. now()
    allitems=items.objects.all()
    return render(request,'gates/gallery.html',{"today":today,"allitems":allitems})
    



def send_email(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    
    if name and email and subject and message:
        message = ('Name: {} \n Email: {} \n Message: {}'.format(name,email,message))
        to_email=settings.EMAIL_HOST_USER
        try:
            send_mail(subject, message, email, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        message='Thank you {} for contacting us. we\'ll get back to you shortly'.format(name)
        today = datetime. now()
        return render(request,'gates/message.html',{'message':message,'today':today})
        #messages.success(request,'Thank you for contacting us. we\'ll get back to you shortly \n <a href="https://hitechcomputers.herokuapp.com/">Go Back Home </a>')
    else:
        
        return HttpResponse('Make sure all fields are entered and valid.')





#views for tarragon medics starts here
def main_home(request):
    return render(request,"index.html")
def index(request):
    today = datetime. now()
    items = shop.objects.all()
    return render(request,"medical/index.html",{"today":today,"items":items})

def aboutus(request):
    today = datetime. now()
    return render(request,"medical/about.html",{"today":today})

def contactus(request):
    today = datetime. now()
    return render(request,"medical/contact-us.html",{"today":today})

def services(request):
    today = datetime. now()
    return render(request,"medical/service.html",{"today":today})

def operating_theatre_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="operating_theatre_equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def ob_gyn_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="OB/GYN_equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})

def diagnostic_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Diagnostic_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def sterilizer(request):
    today = datetime. now()
    items = shop.objects.filter(category="Sterilizer_(Autoclave)")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def laboratory_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Laboratory_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def xray_series(request):
    today = datetime. now()
    items = shop.objects.filter(category="X-ray_Series")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def invitro_diagnostics(request):
    today = datetime. now()
    items = shop.objects.filter(category="In-Vitro_Diagnostics")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def hospital_furniture(request):
    today = datetime. now()
    items = shop.objects.filter(category="Hospital_Furniture")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def walking_aids(request):
    today = datetime. now()
    items = shop.objects.filter(category="Walking_Aids")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def firstaid_products(request):
    today = datetime. now()
    items = shop.objects.filter(category="First-Aid_Products")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def ophthalmic_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Ophthalmic_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def dental_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Dental_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def ent_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="ENT_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def home_care_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Home_Care_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    

def veterinary_equipment(request):
    today = datetime. now()
    items = shop.objects.filter(category="Veterinary_Equipment")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
def medical_consumables(request):
    today = datetime. now()
    items = shop.objects.filter(category="Medical_Consumables")
    instagram = shop.objects.all()
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})

def store(request):
    today = datetime.now()
    items = shop.objects.all()
    instagram = items
    return render(request,"medical/shop.html",{"today":today,"items":items,"instagram":instagram})
    
    



def shop_details(request,slug,category):
    today = datetime. now()
    item = get_object_or_404(shop,slug=slug)
    items = shop.objects.all()
    category = item.category
    return render(request,"medical/shop-detail.html",{"item":item,"items":items,"today":today})
