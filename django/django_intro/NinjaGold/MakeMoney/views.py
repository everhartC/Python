from django.shortcuts import render, redirect
from datetime import datetime
import random

# Create your views here.
def home(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'home.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['place'] == 'farm':
            gold = random.randrange(10,20)
            request.session['activities'].append(
                'Earned ' + str(gold) + ' gold from the farm! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.now())
            )
        elif request.POST['place'] == 'cave':
            gold = random.randrange(5,10)
            request.session['activities'].append(
                'Earned ' + str(gold) + ' gold from the cave! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.now())
            )
        elif request.POST['place'] == 'house':
            gold = random.randrange(5,10)
            request.session['activities'].append(
                'Earned ' + str(gold) + ' gold from the house! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.now())
            )
        elif request.POST['place'] == 'casino':
            gold = random.randint(-50,51)
            if gold >= 0:
                request.session['activities'].append(
                    'Earned ' + str(gold) + ' gold from the house! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.now())
            )
            else:
                request.session['activities'].append(
                    'Lost ' + str(gold) + ' gold from the house! Uh oh! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.now())
            )
        request.session['total_gold'] += gold
    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return redirect('/')