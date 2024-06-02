from django.shortcuts import render, redirect
from .forms import RegisterAndLoginForm, TraderAuthenticationForm
from .models import Trader
from django.contrib import messages


def register(request):
    form = RegisterAndLoginForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RegisterAndLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                Trader().register(username, password)
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

            if Trader.login(request, username, password):
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
            user.authenticate_user(phone_number, credit_card)

            messages.success(request, 'احراز هویت با موفقیت انجام شد!')
            return redirect('login')

    return render(request, 'authentication.html', context)


def logout(request):
    Trader.logout(request)
    return redirect('login')


def home(request):
    return render(request, 'base.html')
