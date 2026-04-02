from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('report/', views.report_fault, name='report_fault'),
    path('delete/<int:fault_id>/', views.delete_fault, name='delete_fault'),
]