from django import forms
from .models import Device


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('category', 'ins_ref', 'fbs_ref', "model", 'serial_number', 'mac_address', 'ip', 'location')