from django.shortcuts import render, redirect
from hashlib import sha1
from models import UserInfo


# Create your views here.
def register(request):

    return render(request, 'tt_user/register.html')


def register_handle(request):

    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    upwd2 = dict.get('cpwd')
    email = dict.get('email')

    if upwd != upwd2:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()

    user=UserInfo()
    user.uname=uname
    user.upwd=upwd_sha1
    user.uemail=email
    user.save()

    return redirect('/user/login/')
