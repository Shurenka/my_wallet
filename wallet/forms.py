from django import forms

from .models import Income, Account, Outcome, Category, Transaction


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('sum', 'account', 'comment', 'date')


class OutcomeForm(forms.ModelForm):
    class Meta:
        model = Outcome
        fields = ('total', 'account', 'category', 'label', 'comment', 'date')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'balance', 'take_into_account')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'planned')


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('total', 'account_from', 'account_to', 'date', 'label', 'comment')
