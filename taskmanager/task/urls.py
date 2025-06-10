from django.urls import path
from task import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'), 
    path('signinform', views.signinform, name='signinform'),
    path('signup', views.signup, name='signup'),
    path('add_user',views.add_user,name='add_user'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_task',views.add_task, name='add_task'),
    path('task', views.task, name='task'),
    path('logout',views.logout,name='logout'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task')
]
