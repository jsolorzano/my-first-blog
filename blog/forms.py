from django import forms

from .models import Post  # En django . significa que se está llamando a un módulo en el mismo directorio

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text')
