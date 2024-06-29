from django.shortcuts import render

def home(request):
    d = {'author':'Rahim',
         'age': 5,
        'lst' : ['pyhton','is','best'],
        'courses' : [
            {
                'id':1,
                'name' : 'python',
                'fee' : 5000
            },
            {
                'id':2,
                'name' : 'django',
                'fee' : 10000
            },
            {
                'id':3,
                'name' : 'C++',
                'fee' : 1000
            }
        ]
    }
    lst = [1,2,3]
    return render(request,'home.html',d)
