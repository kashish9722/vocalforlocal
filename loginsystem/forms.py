from django import forms

from .models import Sample1, pSELLER

class Sample1form(forms.ModelForm):
    class Meta:
        
        model = Sample1
        fields = ('flname', 'email','pnumber','password','repassword',)  
class pSELLERform(forms.ModelForm):
    class Meta:
        
        model = pSELLER
        fields = ('username','flname', 'email','pnumber','password','repassword','city','state','zip','address','iurl','desc')  