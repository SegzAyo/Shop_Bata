from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    categories = forms.ChoiceField(choices=Product.CATEGORY_CHOICES)

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'