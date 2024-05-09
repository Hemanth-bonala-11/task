from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Bank

def insert_data(request):
    df = pd.read_csv('bank_branches.csv')

    data = df.to_dict('records')
    instances = [Bank(**row) for row in data]

    Bank.objects.bulk_create(instances)


    return HttpResponse("<h1> inserted data in db successfully</h1>")

def welcome(request):

    return HttpResponse("<h1> Hemanth Bonala's Task submission for backend </h1>")
