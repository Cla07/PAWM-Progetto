from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Auto
from .forms import AutoForm
from django.views.generic import ListView, DetailView

import pyrebase #libreria pyrebase4 
from django.contrib import auth
import os

#Configurazione fireBase 
config = {
  "apiKey": os.getenv('APIKEY'), 
  "authDomain": os.getenv('AUTH_DOMAIN'), 
  "projectId": os.getenv('PROJECT_ID'),
  "storageBucket": os.getenv('STORAGE_BUCKET'), 
  "messagingSenderId": os.getenv('MESSAGING_SENDER_ID'), 
  "appId": os.getenv('APP_ID'), 
  "measurementId": os.getenv('MEASUREMENT_ID') ,
  "databaseURL" : os.getenv('DATABASE_URL'), 
}

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()  #database Firebase 

# Create your views here.
def home (request):
    return render(request,'home.html')
    
def auto (request):
    return render(request,'auto.html')

#Definisco le rotte REST per le auto 
def login(request) : 
    return render(request, 'login.html')


#rotta post Login (torno alla home se login andato a buon fine)
def postLogin(request) :
    email = request.POST.get('email')
    password = request.POST.get("password") #deve corrispondere con il nome nella vista 
    try:
        user = auth.sign_in_with_email_and_password(email, password)
    except:
        message="Credenziali errate"
        return render(request, "login.html", {"message": message})
   
    session_id = user['idToken']
    request.session['uid']=str(session_id)
    return render(request, 'home.html', {"e": email})

def logout(request):
    auth.logout(request)
    return render(request, "login.html")

#registrazione
def registration(request):
    return render(request,'registration.html')

def postRegistration(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        # creazione di un utente con email e password 
        user=auth.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
    except:
        return render(request, 'registration.html')
    return render(request,'login.html')

#restituisce tutte le auto 
@api_view(['GET'])
def getListaAuto(request):
    auto = Auto.objects.all()
    return render(request,'auto.html', {'auto':auto} )

#ROTTE 
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'listaAuto'

    def get_queryset(self):
        return Auto.objects.all()

class AutoDetailView(DetailView):
    model = Auto
    template_name = 'dettagliAuto.html'

#Creazione di una nuova auto    
def postAuto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = AutoForm()

    return render(request,'postAuto.html',{'form': form})

#Aggiornamento di un'auto 
def putAuto(request, pk, template_name='putAuto.html'):
    auto = get_object_or_404(Auto, pk=pk)
    form = AutoForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Eliminazione di un'auto
def deleteAuto(request, pk, template_name='confirm_delete.html'):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method=='POST':
        auto.delete()
        return redirect('index')
    return render(request, template_name, {'object':auto})


def cercaAuto(request):
    if request.method == 'POST':
        ricercata = request.POST['ricercata']
        auto = Auto.objects.filter(marca__contains=ricercata)
        return render (request,'cercaAuto.html', {'ricercata':ricercata, 'auto':auto})

 

