from django import forms


PERMISSION_TYPE = (
    ('Access Denied', 'Access Denied'),
    ('Can View', 'Can View'),
    ('Can Edit', 'Can Edit'),
)
CURRENCY_TYPE = (
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('VND', 'VND'),
)
STAY_TYPE_M = (
    ('Daily', 'Daily'),
)
STAY_TYPE_SM = (
    ('Hourly', 'Hourly'),
    ('Overnight', 'Overnight'),
    ('Daily', 'Daily'),
)
CODE_TYPE = (
    ('GBP / AUD', 'GBP / AUD'),
    ('EUR / JPY', 'EUR / JPY'),
    ('GOLD', 'GOLD'),
    ('BITCOIN', 'BITCOIN'),
)

DATE_TYPE = (
    ('20-06-17', '2020년 6월 17일'),
    ('20-06-18', '2020년 6월 18일'),
    ('20-06-19', '2020년 6월 19일'),
    ('20-06-20', '2020년 6월 20일'),
)


class ChartForm(forms.Form):
    date = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_date", 'onChange': "selectChange()"}),
        choices=DATE_TYPE, initial='20-06-20',
    )
    code = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_code", 'onChange': "selectChange()"}),
        choices=CODE_TYPE, initial='GBP / AUD',
    )
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': "form-control"}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile', 'class': "form-control"}))
    permission_dashboard = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Business',
    )
    permission_hotel_information = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can View',
    )
    permission_hotel_room = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can View',
    )
    permission_hotel_extra_product = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can View',
    )
    permission_hotel_facility = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can View',
    )
    permission_management_staff = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Access Denied',
    )
    permission_management_customer = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can Edit',
    )
    permission_payment = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can Edit',
    )
    permission_connectivity = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Access Denied',
    )
    permission_booking = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Can Edit',
    )
    permission_report = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=PERMISSION_TYPE, initial='Access Denied',
    )