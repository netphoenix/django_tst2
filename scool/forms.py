from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AddCourseForm(forms.Form):
    langs = [
        ("py", "Python"),
        ("ls", "JavaScript"),
        ("an", "Android"),
        ("fr", "FrontEnd")
    ]

    name = forms.ChoiceField(choices=langs, label="Наименование")
    course_num = forms.IntegerField(max_value=25, min_value=1)
    start_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'type':'date',
            'placeholder':'11:22:3333'
        }
    ))
    end_date = forms.DateField(widget=forms.SelectDateWidget)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'colls':30, 'rows':5}),
        required=False
    )
    # user = forms.ModelChoiceField(
    #     queryset = Person.objects.all(),
    #     empty_label = 'Пользователь не выбран'
    # )

class AddCourseForm2(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['name', 'course_num']

        widgets = {
            'start_date':forms.DateInput(
                attrs={'type':'date', 'class':'data_label'}
            )
        }

class AddUserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ['name', 'course_num']
    def clean_age (self):
        age = self.cleaned_data['age']
        if age == 22 or age == 33:
            raise ValidationError('Возраст не подходит')
        return age
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логинэ',
        widget=forms.TextInput(attrs={'class':'class1'})
    )
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'password1']
    