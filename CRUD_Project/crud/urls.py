from django.urls import path
from crud.views import base, update, add, delete_data

urlpatterns = [
   path('base/',base,name='base'),
   path('add/',add, name='add'),
   path('update/<int:id>/', update, name='update'),
   path('delete/<int:id>/', delete_data , name='delete_data')
] 