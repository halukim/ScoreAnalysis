from django import forms
from . import models

CODE_TYPE = (
    # ('GBP/AUD', 'GBP/AUD'),
    # ('EUR/JPY', 'EUR/JPY'),
    # ('GOLD', 'GOLD'),
    ('BITCOIN', 'BITCOIN'),
)

DATE_TYPE = (
    ('2020-06-17', '2020년 6월 17일'),
    ('2020-06-18', '2020년 6월 18일'),
    ('2020-06-19', '2020년 6월 19일'),
    ('2020-06-20', '2020년 6월 20일'),
    ('2020-06-21', '2020년 6월 21일'),
    ('2020-06-22', '2020년 6월 22일'),
    ('2020-06-23', '2020년 6월 23일'),
    ('2020-06-24', '2020년 6월 24일'),
    ('2020-06-25', '2020년 6월 25일'),
    ('2020-06-26', '2020년 6월 26일'),
)

HOUR_TYPE = [
    ('00', '0시'),
    ('01', '1시'),
    ('02', '2시'),
    ('03', '3시'),
    ('04', '4시'),
    ('05', '5시'),
    ('06', '6시'),
    ('07', '7시'),
    ('08', '8시'),
    ('09', '9시'),
    ('10', '10시'),
    ('11', '11시'),
    ('12', '12시'),
    ('13', '13시'),
    ('14', '14시'),
    ('15', '15시'),
    ('16', '16시'),
    ('17', '17시'),
    ('18', '18시'),
    ('19', '19시'),
    ('20', '20시'),
    ('21', '21시'),
    ('22', '22시'),
    ('23', '23시'),
]


class ChartForm(forms.Form):
    code = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_code", 'onChange': "selectChange()"}),
        choices=CODE_TYPE, initial='GBP / AUD',
    )
    date = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_date", 'onChange': "selectChange()"}),
        choices=DATE_TYPE, initial='20-06-20',
    )
    hour = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_hour", 'onChange': "selectChange()"}),
        choices=HOUR_TYPE, initial='9',
    )
