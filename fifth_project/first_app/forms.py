from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name',help_text="Total length must be 70 characters",required=False)
    file = forms.FileField()  
    email = forms.EmailField(label='User Email')
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    meal = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname)<10:
#             raise forms.ValidationError("Need atleast 10 character")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com in it")

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Enter a name with aleast 10 characters')])
    email = forms.CharField(widget=forms.EmailInput)
    age = forms.CharField(widget=forms.NumberInput)

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        
        if val_conpass != val_pass:
            raise forms.ValidationError("Passowrds dont match!")
        if len(val_name) < 10:
            raise forms.ValidationError("Name length must be greater than 10")