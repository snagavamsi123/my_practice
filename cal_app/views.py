from datetime import datetime
from django.shortcuts import redirect, render
import calendar
from calendar import HTMLCalendar
import datetime
from .models import Event

def home(request):
    if request.method=='POST':

        month=request.POST['month']
        year = int(request.POST['year'])

        month_number = list(calendar.month_name).index(month)
        cal = HTMLCalendar().formatmonth(year,month_number)
        year= year
        month = month

        return redirect(index,year=year,month=month)
    else:
        return render(request,'home.html')

def index(request,month,year):

    if request.method=='POST':
        
        month=request.POST['month']
        year = request.POST['year']
        if ((year is not None) and (year.isdigit() == False)):
            year=datetime.date.today().year
        year=int(year)
        month_number = list(calendar.month_name).index(month)
        cal = HTMLCalendar().formatmonth(year,month_number)
        
        year= year
        month = month
        return redirect(index,year=year,month=month)

    month_number = list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year,month_number)
    year= year
    month = month

    return render(request,'home.html',{'month':month,'year':year , 'cal':cal})

def events(request):
    events= Event.objects.all()
    return render(request,'events.html',{'events':events})





