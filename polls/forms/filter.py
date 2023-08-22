from django import forms
import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class FilterForm(forms.Form):
    initialDate =datetime.date(year=2020, month=6, day=8)
    fecha = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'), initial=initialDate)

    #fecha = forms.DateField(widget=DatePickerInput(format='%m/%d/%Y'), initial=datetime.date.today)
