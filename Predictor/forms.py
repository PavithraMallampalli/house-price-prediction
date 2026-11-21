from django import forms
from .pricing_data import LOCATION_PRICES, FURNISHING_ADJUSTMENT

# Dropdown options are built from our pricing file,
# so a new city added there appears in the form automatically.
LOCATION_CHOICES = [(city, city) for city in LOCATION_PRICES]
FURNISHING_CHOICES = [(status, status) for status in FURNISHING_ADJUSTMENT]


class PredictionForm(forms.Form):
    location = forms.ChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    area = forms.IntegerField(
        label="Area (sq ft)",
        min_value=100,
        max_value=10000,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 1000'})
    )
    bhk = forms.IntegerField(
        label="Number of Bedrooms (BHK)",
        min_value=1,
        max_value=6,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2'})
    )
    bathrooms = forms.IntegerField(
        label="Number of Bathrooms",
        min_value=1,
        max_value=6,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2'})
    )
    property_age = forms.IntegerField(
        label="Property Age (years)",
        min_value=0,
        max_value=50,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 5'})
    )
    furnishing = forms.ChoiceField(
        label="Furnishing Status",
        choices=FURNISHING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # Extra validation that checks two fields together
    def clean(self):
        cleaned_data = super().clean()
        bhk = cleaned_data.get('bhk')
        bathrooms = cleaned_data.get('bathrooms')

        if bhk and bathrooms and bathrooms > bhk + 1:
            self.add_error('bathrooms', "Bathrooms cannot be more than BHK + 1.")

        return cleaned_data