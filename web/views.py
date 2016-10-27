from django.shortcuts import render_to_response
from web.models import User
# Create your views here.

def login(req):
    if req.method == "GET":
        return render_to_response('login.html')
    else:
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        users = User.objects.filter(username__exact=username, password__exact=password)
        if len(users)>0:
            user = users[0]
        else:
            users = User.objects.filter(phone__exact=username, password__exact=password)
            if len(users)>0:
                user = users[0]
            else:
                user = User.objects.filter(email__exact=username, password__exact=password)
                if len(users) > 0:
                    user = users[0]
                else:
                    user = None
        if user is None:
            return render_to_response('login.html', {'msg': '用户名或者密码错误'})

