from django import forms
from django.core.exceptions import ValidationError
from .models import BurnSettings

class BurnSettingsForm(forms.Form):
    set_boiler_temp = forms.IntegerField(initial=50,
                                         min_value=1, 
                                         max_value=90,
                                         widget=forms.NumberInput(attrs={'style': 'width:180px'}),
                                         help_text='value in celcius')
    
    work_feed = forms.IntegerField(initial=10,
                                   min_value=1,
                                   widget=forms.NumberInput(attrs={'style': 'width:180px'}),
                                   help_text='value in seconds')
    
    work_pause = forms.IntegerField(initial=60,
                                    min_value=1,
                                    widget=forms.NumberInput(attrs={'style': 'width:180px'}),
                                    help_text='value in seconds')
    
    work_power = forms.IntegerField(initial=100,
                                    min_value=1,
                                    max_value=100,
                                    widget=forms.NumberInput(attrs={'style': 'width:180px'}),
                                    help_text='value in percents %')
    
    def clean_set_boiler_temp(self):
        boiler_temp = self.cleaned_data['set_boiler_temp']
        
        if not isinstance(boiler_temp, int):
            raise ValidationError('Boiler temp is not a number')
        
        return boiler_temp  