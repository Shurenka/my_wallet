from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Account, Category
from .forms import IncomeForm, AccountForm, OutcomeForm, CategoryForm, TransactionForm


def all_accounts(request):
    accounts = Account.objects.all().order_by('pk')
    balance = Account.objects.filter(take_into_account=True)\
        .aggregate(Sum('balance'))['balance__sum']
    categories = Category.objects.all()
    return render(request, 'wallet/all_accounts.html',
                  {'accounts': accounts, 'balance': balance,
                   'categories': categories})


def account_new(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('all_accounts')
    else:
        form = AccountForm()
    return render(request, 'wallet/account_edit.html', {'form': form})


def income_new(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.date = timezone.now()
            income.account.increase(income.sum)
            income.save()
            return redirect('all_accounts')
    else:
        form = IncomeForm()
    return render(request, 'wallet/income_edit.html', {'form': form})


def outcome_new(request):
    if request.method == "POST":
        form = OutcomeForm(request.POST)
        if form.is_valid():
            outcome = form.save(commit=False)
            outcome.date = timezone.now()
            outcome.account.decrease(outcome.total)
            outcome.save()
            return redirect('all_accounts')
    else:
        form = OutcomeForm()
    return render(request, 'wallet/outcome_edit.html', {'form': form})


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('all_accounts')
    else:
        form = CategoryForm()
    return render(request, 'wallet/category_edit.html', {'form': form})


def transaction_new(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account_from.decrease(transaction.total)
            transaction.account_to.increase(transaction.total)
            transaction.save()
            return redirect('all_accounts')
    else:
        form = TransactionForm()
    return render(request, 'wallet/transaction_edit.html', {'form': form})


def account_edit(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('all_accounts')
    else:
        form = AccountForm(instance=account)
    return render(request, 'wallet/account_edit.html', {'form': form})


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'wallet/all_categories.html',
                  {'categories': categories})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('all_categories')
    else:
        form = AccountForm(instance=category)
    return render(request, 'wallet/category_edit.html', {'form': form})
