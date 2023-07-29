
from django.urls import include, path
from django.urls import path

from bankApp import views
app_name='bankApp'

urlpatterns = [

    path('',views.allBranches,name='allBranches'),
    path('<slug:b_slug>/', views.allBranches, name='Branches'),
    path('<slug:b_slug>/<slug:sub_br_slug>/', views.sub_branches, name='sub_branches'),

]

