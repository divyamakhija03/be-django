from django.urls import path
from . import views



urlpatterns = [
    path('home/',views.home,name='home'),
    path('womenwelfare/',views.womenwelfare,name='womenwelfare'),
    path('grievance/',views.grievance,name='grievance'),
    path('utility/',views.utility,name='utility'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),

    
]