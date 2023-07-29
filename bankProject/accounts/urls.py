from django.urls import include, path
from django.urls import path

from accounts import views
app_name ='accounts'

urlpatterns = [

    path( 'create_account', views.create_account, name= 'create_account'),
    path('details/',views.details,name='details'),

]
