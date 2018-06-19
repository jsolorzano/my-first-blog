from django.shortcuts import render
from django.utils import timezone
from .models import Post  # En django . significa que se está llamando a un módulo en el mismo directorio

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
