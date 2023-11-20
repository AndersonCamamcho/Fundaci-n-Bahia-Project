from django import forms
from .models import Beneficiary


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = [
             'name',
             'lastName',
             'email',
             'identification',
             'birthdate',
        ]



