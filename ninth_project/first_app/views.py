from django.shortcuts import render
from django.urls import HttpResponse
from datetime import datetime,timedelta

def home(request):
    response = render(request,'home.html')
    response.set_cookie('name','Randi')
    # response.set_cookie('name','Rand',max_age=10)
    response.set_cookie('name','Rand',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})

def del_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response 

def set_session(request):
    data = {
        'name' : 'Rand_reborn',
        'age': 23,
        'language' : 'Bangla'
    }
    request.session.update(data)
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        request.session.modified = True
        return render(request,'get_session.html',{'name':name})
    else:
        return HttpResponse("Session Expired.Login Again.")

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'del.html')