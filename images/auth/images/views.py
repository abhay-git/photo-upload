from django.shortcuts import render, redirect
from .forms import ImageCreateForm
from django.contrib import messages
# Create your views here.

def image_create(request):
	if request.method == 'POST':
		form = ImageCreateForm(data=request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_item = form.save(commit=False)

			new_item.user = request.user
			new_item.save()
			messages.success(request, 'Image added successfully')

			return redirect(new_item.get_absolute_url())
	else:
		form = ImageCreateForm(data=request.GET)

	return render(request,'images/image/create.html',{'section':'images','form':form})
