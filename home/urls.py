from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.simple_upload, name='upload'),
    path('temp-data/', views.temp_data, name='temp-data'),
    path('all-data/', views.all_data, name='all-data'),
    path('send-data/', views.send_data, name='send-data'),
    path('update-table/<int:id>', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]
