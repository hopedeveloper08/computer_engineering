from django import forms


class RegisterAndLoginForm(forms.Form):
    username = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'})
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'})
    )


class TraderAuthenticationForm(forms.Form):
    phone_number = forms.CharField(
        max_length=11,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'})
    )
    credit_card = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'شماره حساب'})
    )
