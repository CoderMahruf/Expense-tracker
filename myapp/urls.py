from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('edit/<int:id>/',views.edit,name='edit'),
]
