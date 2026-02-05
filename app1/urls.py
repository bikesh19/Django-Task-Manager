from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_view,name='register'),
     path('login/',views.login_view,name='login'),
      path('logout/',views.logout_view,name='logout'),
       path('', views.dashboard_view, name='dashboard'),
    path('update/<int:id>/', views.task_update, name='task_update'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
    path('complete/<int:id>/', views.task_complete, name='task_complete'),
]
