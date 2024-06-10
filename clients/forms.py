from django import forms 
# from django.contrib.auth.models import User
from clients.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de User ", max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña ", max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','address','area_number','phone')
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})

        self.fields['username'].label = "Nombre de Usuario "
        self.fields['password'].label = "Contraseña "
        self.fields['email'].label = "Correo Electronico"
        self.fields['first_name'].label = "Nombres"
        self.fields['last_name'].label = "Apellidos"
        self.fields['address'].label = "Direccion " 
        self.fields['area_number'].label = "Codigo Postal" 
        self.fields['phone'].label = "Celular" 
        self.fields['username'].help_text = ""
        self.fields['username'].error_messages['unique'] = 'Este nombre de usuario ya existe'
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(message='Este correo electrónico ya está en uso', code='unique')
        return email

    def clean_phone(self):  
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise ValidationError(message='Este número de teléfono ya está en uso', code='unique')
        return phone