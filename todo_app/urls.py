from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reminder/', views.reminder, name='reminder'),
    path('about/', views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    path('complete/<id>', views.complete, name='complete'),
    path('pending/<id>', views.pending, name='pending'),
]
