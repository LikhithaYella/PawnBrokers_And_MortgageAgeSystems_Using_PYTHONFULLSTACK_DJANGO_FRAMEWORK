from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import CRegistrationForm,  PawnbrokerForm
from .models import Customer,Pawnbroker,Admin

def home(request):
    return render(request, "index.html")


def cregistration(request):
    form = CRegistrationForm()
    if request.method == "POST":
        formdata = CRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg="Customer Registered Successfully"
            return render(request, "cregistration.html", {"cform": form,"msg":msg})
        else:
            msg = "Failed to Register Customer"
            return render(request, "cregistration.html", {"cform": form, "msg": msg})
    return render(request,"cregistration.html",{"cform":form})



def clogin(request):
    return render(request,"clogin.html")

def checkclogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    flag = Customer.objects.filter(Q(username=uname) & Q(password=pwd))

    print(flag)

    if flag:
        emp = Customer.objects.get(username=uname)
        print(emp)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "chome.html", {"eid": emp.id, "ename": emp.fullname})
    else:
        msg = "Login Failed"
        return render(request, "clogin.html", {"msg": msg})


def chome(request):
    eid=request.session["eid"]
    ename=request.session["ename"]

    return render(request,"chome.html",{"eid":eid,"ename":ename})

def cprofile(request):
    eid=request.session["eid"]
    ename=request.session["ename"]
    emp = Customer.objects.get(id=eid)
    return render(request,"cprofile.html",{"eid":eid,"ename":ename,"emp":emp})


def clogout(request):
    return render(request,"clogin.html")

def about(request):
    return render(request,"about.html")


















def addpawnbroker(request):
    auname = request.session["auname"]
    form = PawnbrokerForm()
    if request.method == "POST":
        formdata = PawnbrokerForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "addpawnbroker.html", {"auname":auname,"pawnbrokerform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addpawnbroker.html", {"auname":auname,"pawnbrokerform": form, "msg": msg})
    return render(request,"addpawnbroker.html",{"auname":auname,"pawnbrokerform":form})


def viewapawnbroker(request):
    auname=request.session["auname"]
    productlist = Pawnbroker.objects.all()
    count = Pawnbroker.objects.count()
    return render(request,"viewapawnbroker.html",{"auname":auname,"productlist":productlist,"count":count})




def alogin(request):
    return render(request,"alogin.html")

def checkadminlogin(request):
    uname = request.POST["username"]
    pwd = request.POST["password"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
    print(flag)

    if flag:
        admin = Admin.objects.get(username=uname)
        print(admin)
        request.session["auname"] = admin.username
        return render(request, "adminhome.html", {"auname": admin.username})
    else:
        msg = "Login Failed"
        return render(request, "alogin.html", {"msg": msg})


def adminhome(request):
    auname=request.session["auname"]
    return render(request,"adminhome.html",{"auname":auname})


def adminlogout(request):
    return render(request,"alogin.html")

def viewcustomers(request):
    auname=request.session["auname"]
    emplist = Customer.objects.all()
    count = Customer.objects.count()
    return render(request,"viewcustomers.html",{"auname":auname,"emplist":emplist,"count":count})

def deletecus(reequest,eid):
    Customer.objects.filter(id=eid).delete()
    return redirect("viewemps")