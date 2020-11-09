from django.urls import path
from .import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.welcome, name='home'),
    path('About-Us/', views.about, name='about'),
    path('ussdapp/', views.ussdapp, name='ussdapp'),
    path('ussdmobi/', views.ussdmobi, name='ussmobi'),
    path('registration/', views.registration,name='register'),
    path('<int:id>/deleteInfos/', views.delreg,name='deleteInfos'),
    path('<int:id>/updateInfos/', views.updatereg,name='updateInfos'),
    path('reg/endpoint/', views.registerEndpoint,name='endpoint'),
    path('deleteEndpoint/<int:id>/', views.deleteEndpoint,name='deleteEndpoint'),
    path('user-login/', CustomAuthToken.as_view()),

    path('account-creation/',views.accountcreation,name='accountcreation')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)