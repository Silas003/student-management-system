from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('view/<str:id>/',views.view,name='view'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')

]