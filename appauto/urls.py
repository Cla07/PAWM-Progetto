from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.login),
    #Percorsi per autenticazione/login
    path('home', views.postLogin), #la pagina dopo la login, se la login va a buon fine torno alla home
    path('registration', views.registration, name="registration"), 
    path('postRegistration', views.postRegistration),
    path('logout', views.logout, name="log"),
   
    #Rotte auto
    path('auto', views.IndexView.as_view(), name='index'),
    path('auto/<int:pk>', views.AutoDetailView.as_view(), name='dettagli'),
    path('auto/getAuto', views.getListaAuto),
    path('cercaAuto', views.cercaAuto, name="cercaAuto"),
    path('auto/postAuto', views.postAuto, name='postAuto'),
    path('auto/putAuto/<int:pk>', views.putAuto, name='putAuto'),
    path('auto/deleteAuto/<int:pk>', views.deleteAuto, name='deleteAuto'),

]