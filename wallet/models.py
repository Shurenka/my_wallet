import django
from django.db import models
from django.db.models import Sum
from django.utils import timezone


class Label(models.Model):
    name = models.CharField(max_length=100)

    def change(self, new_name):
        self.name = new_name
        self.save()

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField(default=0)
    take_into_account = models.BooleanField(default=True)

    def change(self, new_name, new_balance, new_state):
        self.name = new_name
        self.balance = new_balance
        self.take_into_account = new_state
        self.save()

    def increase(self, amount):
        self.balance += amount
        self.save()

    def decrease(self, amount):
        self.balance -= amount
        self.save()

    def __str__(self):
        return self.name


class Income(models.Model):
    sum = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField(default=django.utils.timezone.now)

    def change(self, new_sum, new_comment, new_account, new_date):
        self.sum = new_sum
        self.comment = new_comment
        self.account = new_account
        self.date = new_date
        self.save()

    def __str__(self):
        return self.sum


class Category(models.Model):
    name = models.CharField(max_length=100)
    planned = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_monthly_outcome(self, month=timezone.now().month):
        #month = 12
        return Outcome.objects.filter(category=self.pk, date__month=month).aggregate(Sum('total'))['total__sum']


class Outcome(models.Model):
    total = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=django.utils.timezone.now)
    label = models.ManyToManyField(Label, blank=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.total) + " - " + self.category.__str__()


class Transaction(models.Model):
    total = models.FloatField()
    account_from = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_from')
    account_to = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_to')
    date = models.DateField(default=django.utils.timezone.now)
    label = models.ManyToManyField(Label, blank=True)
    comment = models.CharField(max_length=200, blank=True, null=True)


