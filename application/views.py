from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView
from application.form import SignupForm,LoginForm,ClientForm
from application.models import Client
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy


# Create your views here.
def home_page(request):
    return render(request,'application/home.html')

class create(View):
    def get(self,request):
        form = SignupForm()
        return render(request,'application/signup.html',{'form':form})
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'application/signup.html',{'form':form})

class Login(View):
    def get(self,request):
        forms = LoginForm()
        return render(request,'registration/login.html',{'forms':forms})

    def post(self,request):
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)

            user = authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,'application/login.html')
        else:
            return render(request,'application/home.html')

class List_view(ListView):
    model = Client

class create_view(View):
    def get(self,request):
        fm = ClientForm()
        return render(request,'application/client_form.html',{'form':fm})

    def post(self,request):
        fm = ClientForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')

class retrive(DetailView):
    model = Client

class update_view(UpdateView):
    model = Client
    fields = ['client_name']

class delete_view(DeleteView):
    model = Client
    success_url = reverse_lazy('list')
