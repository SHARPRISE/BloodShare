from django import forms

from blood_alert.models import Alert, BLOOD_TYPES

class AddAlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ('name', 'blood_type', 'phone', 'location', 'message')
        name = forms.CharField(label='Enter your name', required=True)
        blood_type = forms.MultipleChoiceField(
            choices=BLOOD_TYPES,
            label='Choose your blood type',
            required=True
            )
        phone = forms.CharField(label='Enter your phone number', required=True)
        location = forms.CharField(label='Enter your location')
        message = forms.CharField(label='Enter a message for details (optional)')

class AddAlertOnlineForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ('location', 'message', 'blood_type')
        location = forms.CharField(label='Enter your location')
        message = forms.CharField(label='Enter a message for details (optional)')
        blood_type = forms.MultipleChoiceField(
                    choices=BLOOD_TYPES,
                    label='Blood type needed',
                    required=True
                    )

class ResolvedAlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ('resolved',)
        resolved = forms.CheckboxInput()
