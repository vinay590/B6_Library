from attr import field
from django import forms
from book.models import Book

# class InputForm(forms.Form):
#     """forms model"""
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length = 200)
#     roll_number = forms.IntegerField(
#                      help_text = "Enter 6 digit roll number"
#                      )
#     password = forms.CharField(widget = forms.PasswordInput())


# print(InputForm())

class InputForm(forms.ModelForm):
    """form using existng model """
    is_published = forms.BooleanField()
    choose = forms.FileField()
    class Meta:
        model = Book   ###existing model book 
        fields = "__all__"
        exclude = {"is_active",} #####tuple mandatory
        


class AddressForm(forms.Form):
    STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
    )

    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("is_active",)