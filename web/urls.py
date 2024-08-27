from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index , name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('departamento/', views.add_dpto, name='add_dpto'),
    path('departamento/<int:id>/', views.edit_dpto, name='edit_dpto'),
    path('extra/add/', views.add_extra, name='add_extra'),
    path('extra/<int:id>/', views.edit_extra, name='edit_extra'),
    path('extra/', views.extra_list, name='extra_list'),
    path('extra/<int:id>/remove/', views.remove_extra, name='remove_extra'),
]