from django.shortcuts import render, redirect
from .forms import RegisterAndLoginForm, TraderAuthenticationForm
from .models import Trader
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout


def register(request):
    form = RegisterAndLoginForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RegisterAndLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                trader = Trader(username=username)
                trader.set_password(password)
                trader.save()
                messages.success(request, 'ثبت نام با موفقیت انجام شد!')
                return redirect('login')
            except:
                messages.error(request, 'ثبت نام با خطا مواجه شد. کاربری با این مشخصات وجود دارد.')

    return render(request, 'register.html', context)


def login(request):
    form = RegisterAndLoginForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RegisterAndLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                dj_login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد!')
            else:
                messages.error(request, 'کاربر با مشخصات وارد شده یافت نشد!اگر حساب کاربری ندارید ثبت نام کنید.')

    return render(request, 'login.html', context)


def authentication(request):
    form = TraderAuthenticationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = TraderAuthenticationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            credit_card = form.cleaned_data['credit_card']

            user = request.user
            user.phone_number = phone_number
            user.credit_card = credit_card
            user.is_auth = True
            user.save()

            messages.success(request, 'احراز هویت با موفقیت انجام شد!')
            return redirect('login')

    return render(request, 'authentication.html', context)


def logout(request):
    dj_logout(request)

    return redirect('login')
