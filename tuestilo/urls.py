from django.urls import path
from  . import views

urlpatterns = [
    path(''             , views.base,         name = 'base'     ),
    path('info'         , views.info,         name = 'info'     ),
    path('catalogo'     , views.catalogo,     name = 'catalogo' ),
    path('contacto'     , views.contacto,     name = 'contacto' ),
    path('carro'        , views.carro,        name = 'carro'    ),
    path('register'     , views.register,     name = 'register' ),
    path('conf_usuario' , views.conf_usuario, name = 'conf_usuario' ),
    path('conf_admin'   , views.conf_admin  , name = 'conf_admin' ),
]