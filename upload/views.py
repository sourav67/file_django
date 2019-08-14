from django.shortcuts import render , redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import FilesForm
from .models import  Files

# Create your views here.
def post_list(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs=FileSystemStorage()
		name= fs.save(uploaded_file.name, uploaded_file)
		url = fs.url(name)
		context['url'] = fs.url(name)
	return render(request, 'upload/upload.html', context )

def files_list(request):
	files = Files.objects.all()
	return render(request , 'files_list.html',{
		'files' :  files
		})	

def upload_file(request):
	if request.method == "POST" :
		form = FilesForm(request.POST , request.FILES)
		if  form.is_valid():
			form.save()
			return redirect('files_list')
	else:
		form = FilesForm()
	return render(request , 'upload_file.html',{
		'form': form 
		})	
