from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_property, name='add_property'),
    path('list/', views.property_list, name='property_list'),
    path('update/<int:property_id>/', views.update_property, name='update_property'),
    path('delete/<int:property_id>/', views.delete_property, name='delete_property'),

]