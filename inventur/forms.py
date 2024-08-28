from django import forms
from django.contrib.auth.models import User
from .models import Location, Boxtyp, Boxitem, Inventur, Inventuritem

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = {'loc_name', 'loc_description', 'boxtyp'}

class BoxitemForm(forms.ModelForm):

    class Meta:
        model = Boxitem
        fields = {'item_name', 'item_amount'}


class BoxtypForm(forms.ModelForm):

    boxitems = forms.ModelMultipleChoiceField(
        label= "Inhalt:",
        queryset = Boxitem.objects.all(),
        widget = forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = Boxtyp
        fields = {'typ_name', 'typ_description', 'boxitems'}



class InventurForm(forms.ModelForm):
     class Meta:
        model = Inventur
        fields = {'inv_name', 'inv_location', 'created_by'}


class InventuritemForm(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['inv_name'].disabled = True
    #    self.fields['item_amount_soll'].disabled = True
        
    class Meta:
        model = Inventuritem
        fields = {'inv_name', 'item_amount_soll', 'item_amount_ist', 'inv_comment'}
