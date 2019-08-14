from django import forms
from .models import Files 

class FilesForm(forms.ModelForm):
	class Meta:
		model = Files 
		fields = ('title','file','created_date','published_date')