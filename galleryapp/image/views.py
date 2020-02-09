from django.shortcuts import render, redirect

from .models import Image
from .forms import ImageCreate
from django.http import HttpResponse


# Create your views here.

def index(request):
    gallery = Image.objects.all()
    return render(request, 'image/gallery.html', {'gallery': gallery})


def upload(request):
    upload = ImageCreate()

    if request.method == 'POST':
        upload = ImageCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""Your form is wrong! Please, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'image/upload_form.html', {'upload_form': upload})


def update_image(request, image_id):
    image_id = int(image_id)
    try:
        image_sel = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        return redirect('index')
    image_form = ImageCreate(request.POST or None, instance=image_sel)
    if image_form.is_valid():
        image_form.save()
        return redirect('index')
    return render(request, 'image/upload_form.html', {'upload_form': image_form})


def delete_image(request, image_id):
    image_id = int(image_id)

    try:
        image_sel = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        return redirect('index')
    image_sel.delete()
    return redirect('index')
