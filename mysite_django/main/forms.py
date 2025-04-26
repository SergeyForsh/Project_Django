from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
