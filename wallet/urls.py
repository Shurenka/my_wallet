from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_accounts, name='all_accounts'),
    path('income/new/', views.income_new, name='income_new'),
    path('account/new/', views.account_new, name='account_new'),
    path('account/<int:pk>/edit/', views.account_edit, name='account_edit'),
    path('outcome/new/', views.outcome_new, name='outcome_new'),
    path('category/new/', views.category_new, name='category_new'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('transaction/new/', views.transaction_new, name='transaction_new'),
    path('categories', views.all_categories, name='categories'),
]
