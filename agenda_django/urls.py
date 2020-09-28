"""agenda_django URL Configuration"""

from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),

    #com o RedirectView.as_view pode se direcionar uma url tambem, assim como a função index
    path('', RedirectView.as_view(url='/agenda/')),

#este url chama o def: login_user que irá direcionar para a pagina login.html
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

    #direcionamentos para controle de eventos
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/', views.evento),
    path('agenda/evento/delete/<int:id_evento>', views.delete_evento)
]
