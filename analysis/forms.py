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


class BotForm(forms.Form):
    bot_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_bot_type", 'onChange': "selectChange()"}),
        choices=BOT_TYPE, initial="PD",
    )
    bot_status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': "form-control", 'id': "select_bot_status", 'onChange': "selectChange()"}),
        choices=BOT_STATUS, initial="ON",
    )
    min_type = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control", 'id': "select_min_type"}),
        choices=MIN_TYPE, initial=["1 Min", "2 Min", "3 Min", "5 Min"]
    )
