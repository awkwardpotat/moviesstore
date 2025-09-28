from django import forms
from .models import Petition

# Form for creating a job post based on add_post.html fields
class PetitionForm(forms.ModelForm):
	class Meta:
		model = Petition
		fields = [
			'name', 'description', 'image', 'reason'
		]
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Enter movie title here', 'class': 'form-control'}),
			'description': forms.TextInput(attrs={'placeholder': 'Enter description here', 'class': 'form-control'}),
			'image': forms.FileInput(attrs={'class': 'form-control'}),
			'reason': forms.TextInput(attrs={'placeholder': 'Enter reason for petition here', 'class': 'form-control'})
	    }