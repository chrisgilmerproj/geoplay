from django.contrib.gis import admin
from django import forms
 
from waypoints.models import Waypoint

# Custom form definition
class WaypointAdminForm(forms.ModelForm):
    # Step 1: Add the extra form fields to the ModelForm
    latitude = forms.FloatField(required=False)
    longitude = forms.FloatField(required=False)
 
    class Meta:
        model = Waypoint
 
    # Step 2: Override the constructor to manually set the form's latitude and
    # longitude fields if a Waypoint instance is passed into the form
    def __init__(self, *args, **kwargs):
        super(WaypointAdminForm, self).__init__(*args, **kwargs)
 
        # Set the form fields based on the model object
        if kwargs.has_key('instance'):
            instance = kwargs['instance']
            self.initial['latitude'] = instance.latitude
            self.initial['longitude'] = instance.longitude 
 
    # Step 3: Override the save method to manually set the model's latitude and
    # longitude properties based on what was submitted from the form
    def save(self, commit=True):
        model = super(WaypointAdminForm, self).save(commit=False)
 
        # Save the latitude and longitude based on the form fields
        model.latitude = self.cleaned_data['latitude']
        model.longitude = self.cleaned_data['longitude']
 
        if commit:
            model.save()
 
        return model

