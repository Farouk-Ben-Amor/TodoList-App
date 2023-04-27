from django import forms

class TodoForm(forms.Form):
    text=forms.CharField(max_length=50,
                         widget=forms.TextInput(
        attrs={'class':'form-control' , 'placeholder':'Enter your todo...',
                'aria-label':'Todo' , 'aria-describedby':'add-btn'}
                         ))
