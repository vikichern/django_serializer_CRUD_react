from django.urls import path
from .views import tasks 

urlpatterns = [
    path('tasks/',tasks ),
    path('tasks/<int:id>',tasks),
]
