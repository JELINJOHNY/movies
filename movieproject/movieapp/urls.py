from django.urls import path

from . import views

urlpatterns = [
    path('',views.testf,name='testf'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')



]