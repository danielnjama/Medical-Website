from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("",views.index,name="index"),
    path("about-us/",views.aboutus,name="aboutus"),
    path("contact-us/",views.contactus,name="contactus"),
    path("store/",views.store,name="store"),
    path("store/operating-theatre-equipment/",views.operating_theatre_equipment,name="operating_theatre_equipment"),
    path("store/ob-gyn-equipment/",views.ob_gyn_equipment,name="ob_gyn_equipment"),
    path("store/diagnostic-equipment/",views.diagnostic_equipment,name="diagnostic_equipment"),
    path("store/sterilizer/",views.sterilizer,name="sterilizer"),
    path("store/laboratory-equipment/",views.laboratory_equipment,name="laboratory_equipment"),
    path("store/xray-series/",views.xray_series,name="xray_series"),
    path("store/in-vitro-diagnostics/",views.invitro_diagnostics,name="invitro_diagnostics"),
    path("store/hospital-furniture/",views.hospital_furniture,name="hospital_furniture"),
    path("store/walking-aids/",views.walking_aids,name="walking_aids"),
    path("store/first-aid-products/",views.firstaid_products,name="firstaid_products"),
    path("store/ophthalmic-equipment/",views.ophthalmic_equipment,name="ophthalmic_equipment"),
    path("store/dental-equipment/",views.dental_equipment,name="dental_equipment"),
    path("store/ent-equipment/",views.ent_equipment,name="ent_equipment"),
    path("store/home-care-equipment/",views.home_care_equipment,name="home_care_equipment"),
    path("store/veterinary-equipment/",views.veterinary_equipment,name="veterinary_equipment"),
    path("store/medical-consumables/",views.medical_consumables,name="medical_consumables"),
    path("search",views.search,name="search"),   

]+ [
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$',views.shop_details,name='shop_details'),
]

