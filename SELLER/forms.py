from django import forms

from .models import  product

# class Psellerform(forms.ModelForm):
#     class Meta:   
#         model = Pseller
#         fields = ('name', 'email','phone','iurl','address') 
class productform(forms.ModelForm):
    class Meta:
        
        model = product
        fields = ('username','iurl', 'img','pname','category','desc') 