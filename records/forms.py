from django import forms
from records.models import Records
from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration


class DurationInput(TextInput):
    def _format_value(self, value):
        duration = parse_duration(value)
        seconds = duration.seconds
        minutes = seconds // 60
        seconds = seconds % 60
        minutes = minutes % 60
        return '{:02d}:{:02d}'.format(minutes, seconds)


class AddRecordForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'add_record__input', 'placeholder': ' 02:07:2023'}))
    # date = forms.DateInput
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'add_record__input', 'placeholder': '9:00'}))
    duration = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'add_record__input', 'placeholder':'1.5'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'add_record__input', 'placeholder': '5000'}))


    class Meta:
        model = Records
        fields = ['date', 'time', 'duration', 'price']





