from django.shortcuts import render
from .models import DetailsOfEvent,Attend
# Create your views here.
from django.contrib.auth import settings
from .models import UserCreation
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import UserCreationForm,OtpForm,LoginForm,SponsorForm,EventForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
def gen_otp():
    import math,random
    OTP=""
    digits="0123456789"
    for i in range(6):
         OTP+=digits[math.floor(random.random()*10)]
    return OTP

random_otp= gen_otp()
msg_body=f"OTP is {random_otp}"
account_sid = 'Enter your account_sid provided bt Twilio'
auth_token = 'Enter your auth token provided by Twilio'
def send_sms(account_sid,account_token,body,from_,to):

    from twilio.rest import Client
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=body,
        from_=from_,
        to=to
    )
def register(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            phone=fm.cleaned_data['phone']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            position=fm.cleaned_data['position']
            send_sms(account_sid,auth_token,msg_body,'+15712235121',phone)
            print("password",password)
            request.session['name']=name
            request.session['phone']=phone
            request.session['email']=email
            request.session['password']=password
            request.session['position']=position

            return HttpResponseRedirect('/otp/')
    else :
        fm=UserCreationForm()
    return render(request,'myapp/register.html',{'form':fm})
def otp(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=OtpForm(request.POST)
            if fm.is_valid():
                otp=fm.cleaned_data['otp']

                if otp == random_otp:
                    user=UserCreation(name=request.session['name'],phone=request.session['phone'],email=request.session['email'],password=request.session['password'],otp=otp,position=request.session['position'])
                    user.save()
                    messages.success(request,'You have successfully signed up')
                    obj_user_creation = UserCreation.objects.all()
                    obj_user = User.objects.all()
                    # print(obj_user_creation)
                    # print(obj_user)
                    li=[]
                    for i in obj_user:
                        li.append(i.username)
                        # print("name",i.username)
                    # print(li)
                    for i in obj_user_creation:
                        if i.name not in li:
                            reg = User(username=i.name, password=i.password)
                            reg.save()
                    return HttpResponseRedirect('/login')
                else:
                    print("otp galat hai babua")
                    messages.error(request,"You have entered a wrong otp")
        else:
            fm=OtpForm()
        return render(request,'myapp/register.html',{'form':fm})
    else:
        messages.success(request,'You must login first')
        return HttpResponseRedirect('/login')
def user_login(request):
    if request.method=="POST":
        fm=LoginForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['password'])
            user=authenticate(username=fm.cleaned_data['name'],password=fm.cleaned_data['password'])
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
    fm=LoginForm()
    return render(request,'myapp/login.html',{'form':fm})
def homepage(request):
    obj=DetailsOfEvent.objects.all()
    return render(request,'myapp/homepage.html',{'obj':obj})
def attend(request):
    if request.user.is_authenticated:
        print(request.user)
        reg=Attend(name=request.user)
        reg.save()
        messages.success(request,'You have successfully enrolled for this event')
        return HttpResponseRedirect('/messages')
    else:
        messages.success(request,"You must login first")
        return HttpResponseRedirect('/login')
def log_out(request):
    logout(request)
    obj = DetailsOfEvent.objects.all()
    messages.success(request,'You have successfully logged out')
    return HttpResponseRedirect('/messages')
def show_messages(request):
    return render(request,'myapp/messages.html')
def sponsor(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=SponsorForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'You have successfully sponsored for this event')
                return render(request,'myapp/messages.html',{'form':fm})
        else:
            fm=SponsorForm()
        return render(request,'myapp/sponsor.html',{'form':fm})
    else:
        messages.success(request,"You must login first")
        return HttpResponseRedirect('/login')
def organise(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=EventForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/')
        else:
            fm=EventForm()
        return render(request,'myapp/organiser.html',{'form':fm})
    else:
        messages.success(request,'You must login first')
        return HttpResponseRedirect('/login')