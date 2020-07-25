from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration,ItemsPrice,OrderDetails
# Create your views here.
def func(request):
    return render(request,'login.html')
def login(request):
    if 'login' in request.POST:
        u=request.POST['uid']
        p=request.POST['pwd']
        all_id=Registration.objects.all()
        for  id in all_id:
            if u == id.email and p == id.password:
                price = ItemsPrice()
                return render(request,'homepage.html',{'id':u,'pass':p,'price':price})
        else:
            return render(request,'login.html')
    elif 'register' in request.POST:
        return render(request,'register.html')
def login1(request):
    name = request.POST['name']
    number = request.POST['number']
    password = request.POST['pass']
    dob = request.POST['dob']
    email = request.POST['email']
    reg=Registration(name=name,email=email,password=password,phone=number,dateofbirth=dob )
    reg.save()
    return render(request, 'login.html')
def order(request):
    if 'e' in request.POST:
        e=request.POST['e']
        sd=request.POST['sd']
        return render(request,'mode_of_trasaction.html',{'dec':sd,'name':e})
    elif 'price' in request.POST:
        price=request.POST['price']
        name=request.POST['name']
        return render(request,'mode_of_trasaction.html',{'dec':price,'name':name})

def itemspage(request):
    price=ItemsPrice()
    return render(request,'itempage.html',{'price':price})

def payment(request):
    temp=request.POST['ram']
    pay=request.POST['price']
    name=request.POST['name']
    if temp=='cd' or temp=='dc':
        return render(request,'credit_card.html',{'pay':pay,'name':name})
    elif temp=='nb':
        return render(request,'net_banking.html',{'pay':pay,'name':name})
    elif temp=='wlt':
        return render(request,'wallet.html',{'pay':pay,'name':name})
def order1(request):
    name=request.POST['name']
    price=request.POST['price']
    ord=OrderDetails(order_name=name,order_price=price)
    ord.save()
    return render(request,'order.html',{'name':name,'price':price})



