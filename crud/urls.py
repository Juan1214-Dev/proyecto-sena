
from django.contrib import admin
from django.urls import path
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home, name='inicio'),

    path('productos', views.consultar, name='consultar'),

    path('productos/guardar', views.guardar, name='guardar'),

    path('productos/eliminar/<int:id> ', views.eliminar, name='eliminar'),

    path('productos/detalle/<int:id> ', views.detalle, name='detalle'),

    path('productos/editar', views.editar, name='editar'),

##################################################################################

    path('usuarios/', views.usuarios, name='usuarios'),

    path('usuarios/guardar', views.guardar_usuario, name='guardar_usuario'),

    path('usuarios/eliminar/<int:id> ', views.eliminar_usuario, name='eliminar_usuario'),

    path('usuarios/detalle/<int:id> ', views.detalle_usuario, name='detalle_usuario'),

    path('usuarios/editar', views.editar_usuario, name='editar_usuario'),

##################################################################################

    path('padres/', views.padres, name='padres'),

    path('padres/guardar', views.guardar_padres, name='guardar_padres'),

    path('padres/eliminar/<int:id> ', views.eliminar_padres, name='eliminar_padres'),

    path('padres/detalle/<int:id> ', views.detalle_padres, name='detalle_padres'),

    path('padres/editar', views.editar_padres, name='editar_padres'),

##################################################################################

    path('ninoabuelos/', views.ninoabuelos, name='ninoabuelos'),

    path('ninoabuelos/guardar', views.guardar_ninoabuelos, name='guardar_ninoabuelos'),

    path('ninoabuelos/eliminar/<int:id> ', views.eliminar_ninoabuelos, name='eliminar_ninoabuelos'),

    path('ninoabuelos/detalle/<int:id> ', views.detalle_ninoabuelos, name='detalle_ninoabuelos'),

    path('ninoabuelos/editar', views.editar_ninoabuelos, name='editar_ninoabuelos'),

##################################################################################

    path('pagos/', views.pagos, name='pagos'),

    path('pagos/guardar', views.guardar_pagos, name='guardar_pagos'),

    path('pagos/eliminar/<int:id> ', views.eliminar_pagos, name='eliminar_pagos'),

    path('pagos/detalle/<int:id> ', views.detalle_pagos, name='detalle_pagos'),

    path('pagos/editar', views.editar_pagos, name='editar_pagos'),

    path("login/", views.login, name="login"),

    path("logout/", views.logout, name="logout"),

    path("cambiar_clave/", views.cambiar_clave, name="cambiar_clave"),

    path("ver_perfil/", views.ver_perfil, name="ver_perfil"),

    path("guardar_clave/", views.guardar_clave, name ="guardar_clave"),

]
