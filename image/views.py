from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ImageForm
from .models import Image

@login_required()
@csrf_exempt
@ require_POST
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            print(JsonResponse({'status': "1"}))
            return JsonResponse({'status':"1"})
        except:
            print(JsonResponse({'status':"0"}))
            return JsonResponse({'status':"0"})
    else:
        print("这是3", JsonResponse({'status': "3"}))
        #<JsonResponse status_code=200, "application/json">
        return JsonResponse({'status': "3"})

@login_required()
def list_images(request):
    images_list = Image.objects.filter(user=request.user)
    paginator = Paginator(images_list, 3)
    page = request.GET.get('page')

    try:
        current_page = paginator.page(page)
        images = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        images = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        images = current_page.object_list
    return render(request, 'image/list_images.html', {"images": images, "page": current_page})

@login_required()
@require_POST
@csrf_exempt
def del_image(request):
    image_id = request.POST['image_id']
    try:
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'status':"1"})
    except:
        return JsonResponse({'status':"2"})

def falls_images(request):
    images = Image.objects.all()
    return render(request, 'image/falls_images.html', {"images": images})