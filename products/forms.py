from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Ask_Complaint, Review



class ProductForm(forms.ModelForm):

    categories = forms.ChoiceField(choices=Product.CATEGORY_CHOICES)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('id',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AskComplaintForm(forms.ModelForm):

    class Meta:
        model = Ask_Complaint
        fields = '__all__'



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text', )       