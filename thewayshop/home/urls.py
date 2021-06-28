from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    
    path("",views.main_home,name="main_home"),
    path("medical/tarragon-medics/",views.index,name="index"),
    path("medical/about-us/",views.aboutus,name="aboutus"),
    path("medical/contact-us/",views.contactus,name="contactus"),
    path("medical/services/",views.services,name="services"),
    path("medical/store.php/",views.store,name="store"),
    path("medical/store/operating-theatre-equipment/",views.operating_theatre_equipment,name="operating_theatre_equipment"),
    path("medical/store/ob-gyn-equipment/",views.ob_gyn_equipment,name="ob_gyn_equipment"),
    path("medical/store/diagnostic-equipment/",views.diagnostic_equipment,name="diagnostic_equipment"),
    path("medical/store/sterilizer/",views.sterilizer,name="sterilizer"),
    path("medical/store/laboratory-equipment/",views.laboratory_equipment,name="laboratory_equipment"),
    path("medical/store/xray-series/",views.xray_series,name="xray_series"),
    path("medical/store/In-vitro-diagnostics/",views.invitro_diagnostics,name="invitro_diagnostics"),
    path("medical/store/Hospital-Furniture/",views.hospital_furniture,name="hospital_furniture"),
    path("medical/store/Walking-Aids/",views.walking_aids,name="walking_aids"),
    path("medical/store/First-Aid-Products/",views.firstaid_products,name="firstaid_products"),
    path("medical/store/Ophthalmic-Equipment/",views.ophthalmic_equipment,name="ophthalmic_equipment"),
    path("medical/store/Dental-Equipment/",views.dental_equipment,name="dental_equipment"),
    path("medical/store/ENT-Equipment/",views.ent_equipment,name="ent_equipment"),
    path("medical/store/Home-Care-Equipment/",views.home_care_equipment,name="home_care_equipment"),
    path("medical/store/Veterinary_Equipment/",views.veterinary_equipment,name="veterinary_equipment"),
    path("medical/store/Medical-Consumables/",views.medical_consumables,name="medical_consumables"),
    
    ##gates urls
    path("automation/tarragon-automation/",views.home, name='home'),
    path("automation/contactus/",views.contact,name='contact'),
    path("automation/send_email/",views.send_email,name='send_email'),
    path("automation/swinging-gates/",views.swinging_gates, name='swinging_gates'),
    path("automation/sliding-gates/",views.sliding_gates, name='sliding_gates'),
    path("automation/garage-gates/",views.garage_gates, name='garage_gates'),
    path("automation/aboutus/",views.about_us,name='about_us'),
    path("automation/cctvs&floodlights/",views.cctv,name='cctv'),
    path("automation/tarragon-gallery/",views.gallery,name='gallery'),
    
    #end of gates urls

   

]+ [
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$',views.shop_details,name='shop_details'),
]

