from django.urls import path 
from . import views 
# current directory se views ko import kro 

urlpatterns = [
   path('list/',views.PlanList.as_view()),   
   path('create/',views.PlanCreate.as_view()),
   path('delete/<int:pk>/', views.PlanDestroy.as_view()),
] 
