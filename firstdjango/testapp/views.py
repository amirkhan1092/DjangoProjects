from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    d = datetime.datetime.now()
    h = int(d.strftime('%H'))
    if h < 12:
        m = 'Good Morning'
    elif h < 16:
        m = 'Good Afternoon'
    elif h < 21:
        m = 'Good Evening'
    else:
        m = 'Good Night'
    return render(request,'testapp/results.html',{'hour':m})