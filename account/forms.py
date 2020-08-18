from django import forms


BOT_TYPE = (
    ("PD", "퐁당퐁당"),
    ("JUL", "줄"),
    ("RANDOM", "램덤"),
    ("COPY", "따라쟁이"),
)
BOT_STATUS = (
    ("ON", "시작"),
    ("OFF", "중지"),
)
MIN_TYPE = (
    ("1 Min", "1 Min"),
    ("2 Min", "2 Min"),
    ("3 Min", "3 Min"),
    ("5 Min", "5 Min"),
)


class SignInForm(forms.Form):
    email = forms.CharField(
        label="email",
        widget=forms.TextInput(attrs={'placeholder': "Email", 'class': "form-control"}))
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control"}))


class SignUpForm(forms.Form):
    email = forms.CharField(
        label="email",
        widget=forms.TextInput(attrs={'placeholder': "Email", 'class': "form-control"}))
    mobile = forms.CharField(
        label="mobile",
        widget=forms.TextInput(attrs={'placeholder': "Mobile", 'class': "form-control"}))
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control"}))
    password_confirm = forms.CharField(
        label="password-confirm",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirm', 'class': "form-control"}))


class PasswordResetForm(forms.Form):
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control"}))
    password_new = forms.CharField(
        label="password-new",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password New', 'class': "form-control"}))
    password_new_confirm = forms.CharField(
        label="password-new-confirm",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password New Confirm', 'class': "form-control"}))


class PasswordForgotForm(forms.Form):
    email = forms.CharField(
        label="email",
        widget=forms.TextInput(attrs={'placeholder': "Email", 'class': "form-control"}))


class UpdateProfileForm(forms.Form):
    email = forms.CharField(
        label="email",
        widget=forms.TextInput(attrs={'placeholder': "Email", 'class': "form-control"}))
    mobile = forms.CharField(
        label="mobile",
        widget=forms.TextInput(attrs={'placeholder': "Mobile", 'class': "form-control"}))
    id_365 = forms.CharField(
        label="id_365",
        widget=forms.PasswordInput(attrs={'placeholder': 'ID for 365', 'class': "form-control"}))
    password_365 = forms.CharField(
        label="password_365",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password for 365', 'class': "form-control"}))
    bitcoin_bot_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=BOT_TYPE, initial="COPY",
        label="bitcoin bot type",
        disabled=False
    )
    bitcoin_bot_status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=BOT_STATUS, initial="OFF",
        label="bitcoin bot status",
        disabled=False
    )
    bitcoin_min_type = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}),
        choices=MIN_TYPE, initial=["1 Min", "2 Min", "3 Min", "5 Min"],
        label="bitcoin min type",
        disabled=False
    )
    gold_bot_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=BOT_TYPE, initial="COPY",
        label="gold bot type",
        disabled=False
    )
    gold_bot_status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=BOT_STATUS, initial="OFF",
        label="gold bot status",
        disabled=False
    )
    gold_min_type = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}),
        choices=MIN_TYPE, initial=["1 Min", "2 Min", "3 Min", "5 Min"],
        label="gold min type",
        disabled=False
    )
