from django.urls import path
from . import views


urlpatterns = [
    path('', views.service, name="service"),
    path('teste/', views.teste, name="teste"),
    path('information/<str:pk>/', views.information, name="information"),
    
    path('create-project/', views.createProject, name="create-project"),
    
    
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
    
]
