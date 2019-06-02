from django.shortcuts import render,redirect
from django.views import generic
from .models import Location
from .models import Property
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'homesapp/index.html'

    def get_queryset(self):
        return Location.objects.all()

class LocationView(generic.DetailView):
    model =  Location
    template_name = 'homesapp/locationview.html'

class PropertyDetail(generic.DetailView):
    model = Property
    template_name = 'homesapp/propertyview.html'


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #log user in
            login(request,user)
            return redirect('/homesapp/')
    else:
        form = UserCreationForm()
    return render(request,'homesapp/signup.html',{'form':form})

def home_view(request):
    return render(request,'homesapp/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login the user
            user = form.get_user()
            login(request,user)
            return redirect('/homesapp/')
    else:
        form = AuthenticationForm()
    return render(request,'homesapp/login.html',{'form':form})

 
    

