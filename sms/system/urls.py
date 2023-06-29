from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('view/<str:id>/',views.view,name='view'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),

]