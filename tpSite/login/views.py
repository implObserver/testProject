from django.shortcuts import render, redirect

from .forms import UserLoginForm
from django.contrib.auth import login


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = UserLoginForm()
    return render(request, 'login/login.html', {"form": form})

