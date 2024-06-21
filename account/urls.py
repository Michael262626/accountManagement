from django.urls import path, include

from django.contrib import admin

from account import views

admin.site.site_header = 'Account Management'

urlpatterns = [
    path('accounts', views.list_accounts),
    path('accounts/<str:pk>/', views.account_details)
]
