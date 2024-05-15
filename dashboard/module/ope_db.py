from django.shortcuts import get_object_or_404
from django.utils.timezone import localtime
from django.utils import timezone
from dashboard.models import Outcome
from dateutil.relativedelta import relativedelta
import pprint

def get():
    return list(Outcome.objects.all().order_by("date").values())

def sum_price():
    l = list()
    month_list = list(Outcome.objects.filter(is_passed=False).dates('date', 'month'))
    #query = Outcome.objects.filter(is_passed=True, created__range=(start_date, end_date))

    for v in month_list:
        tmp = Outcome.objects.filter(is_passed=False, date__gte=v, date__lt=v+relativedelta(months=+1)).values()
        result = 0
        for w in tmp:
            result += w["price"]
        l.append({v : result})

    return l

def write(title, date, price, note):
    Outcome.objects.create(
        title=title,
        date=date,
        price=price,
        note=note
    )

def update(Id, title=None, date=None, price=None, note=None):
    result = get_object_or_404(Outcome, pk=Id)

    if title is not None:
        result.title=title
    if date is not None:
        result.date=date
    if price is not None:
        result.price=price
    if note is not None:
        result.note=note

    result.save()

def delete(Id):
    result = Outcome.objects.get(id=Id)
    result.delete()

def sum_price():
    l = list()
    month_list = list(Outcome.objects.filter(is_passed=False).dates('date', 'month'))
    #query = Outcome.objects.filter(is_passed=True, created__range=(start_date, end_date))
    for v in month_list:
        #l.append([v, list(Outcome.objects.filter(is_passed=True, date__gte=v, date__lt=v+relativedelta(months=+1)).values())])
        print(Outcome.objects.filter(is_passed=False, date__gte=v, date=v+relativedelta(months=+1)))
        #print(Outcome.objects.filter(is_passed=False, date__gte=v, date__lt=v+relativedelta(months=+1)).values())
        #print("date = {} : dict = {}".format(v, Outcome.objects.filter(is_passed=False, date__gte=v, date__lt=v+relativedelta(months=+1)).values()))
