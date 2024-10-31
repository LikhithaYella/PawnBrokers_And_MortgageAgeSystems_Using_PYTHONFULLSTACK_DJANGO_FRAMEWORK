from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
     path("",views.home,name="home"),
    path("cregistration",views.cregistration,name="cregistration"),
    path("clogin",views.clogin,name="clogin"),
    path('clogout',views.clogout,name='clogout'),
    path('checkclogin',views.checkclogin,name="checkclogin"),
    path('chome',views.chome,name="chome"),
    path('cprofile',views.cprofile,name="cprofile"),



    path("addpawnbroker",views.addpawnbroker,name="addpawnbroker"),

    path('viewapawnbroker',views.viewapawnbroker,name="viewapawnbroker"),


    path('alogin',views.alogin,name='alogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('adminlogout', views.adminlogout, name='adminlogout'),
    path('viewcustomers',views.viewcustomers,name="viewcustomers"),
    path("deletecus/<int:eid>",views.deletecus,name="deletecus"),
    path('about',views.about,name="about"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



