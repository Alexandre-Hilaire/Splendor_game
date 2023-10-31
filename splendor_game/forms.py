from django import forms


class ThreeCoinsForm(forms.Form):
    red = forms.BooleanField(label="red", required=False)
    green = forms.BooleanField(label="green", required=False)
    blue = forms.BooleanField(label="blue", required=False)
    white = forms.BooleanField(label="white", required=False)
    black = forms.BooleanField(label="black", required=False)
