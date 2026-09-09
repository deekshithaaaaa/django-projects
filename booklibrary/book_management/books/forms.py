from django import forms
from . models import Books
class BookForm(forms.Form):
    title=forms.CharField(label="Book Title")
    author=forms.CharField(label="Author Name",help_text="Enter the author's name")
    price=forms.IntegerField(initial=500,min_value=100,max_value=5000)
    description=forms.CharField(widget=forms.Textarea,required=False)
    email=forms.EmailField()
    terms=forms.BooleanField()
    catogory=forms.ChoiceField(
        choices=[
            ('fiction','Fiction'),
            ('science','Science'),
            ('history','History'),
            ('biography',"Biography")
        ] 
    )
    languages=forms.MultipleChoiceField(
        choices=[
            ('english','English'),
            ('hindi','Hindi'),
            ('telugu','Telugu')
        ]
    )
    published_date=forms.DateField()
class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'
