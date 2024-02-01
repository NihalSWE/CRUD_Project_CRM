from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('add',views.add,name="add"),
    path('update/<int:pk>',views.update,name='update'),
    path('view/<int:pk>',views.view,name='view'),
    path('delete/<int:pk>',views.delete,name='delete'),
]