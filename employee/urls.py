from django.contrib import admin
from django.urls import path,include
from.import views
from.views import *

# urlpatterns = [
#    path('',views.emp_home),
#    path('add_emp',add_emp ,name='add_emp'),
   
# ]
urlpatterns = [
    path('', views.emp_home, name='emp_home'),  # Or adjust to match the correct view and URL pattern
    path('add_emp', views.add_emp, name='add_emp'),
    path('view_emp', views.view_emp,name='view_emp'),
    path("delete_emp/<int:id>", views.delete_emp, name='delete_emp'),
    path('update_emp/<int:emp_id>', views.update_emp, name='update_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
]              