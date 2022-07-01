from django.urls import path
from . import  views
from .models import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('my_blogs',views.myblogs, name= 'my_blogs'),
    path('publish_blog',views.publishblog, name='publish_blog'),
    path('my_blogs/edit_blog/<int:pk>',views.editblog, name= 'edit_blog'),
    path('my_blogs/delete_blog/<int:pk>',views.deleteblog, name= 'delete_blog'),
    path('blog/<str:pk>/', views.detailview, name= 'detailview'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name= 'password_reset'),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_sent.html'), name= 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'), name= 'password_reset_complete'),
]