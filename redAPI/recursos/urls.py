from django.conf.urls import url

from . import views

urlpatterns = [

    url('', views.ListaRecursos.as_view()),

]