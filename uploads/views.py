from django.shortcuts import render
from django import template
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.template import Template
from django.http import HttpResponse
from django.http import JsonResponse
from .models import File
from accounts.models import Profile
from django.core.files import File as DjangoFile
import os

# Create your views here.

@csrf_exempt
def home(request):
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

@csrf_exempt
def upload(request):

    if request.method == 'POST':

        dir=request.FILES
        dirlist=dir.getlist('files')
        pathlist=request.POST.getlist('paths')
        print(dir)
        if not dirlist:
            return HttpResponse( 'files not found')
        else:

            for file in dirlist:
                position = os.path.join(os.path.abspath(os.path.join(os.getcwd(),'projects')),'/'.join(pathlist[dirlist.index(file)].split('/')[:-1]))
                if not os.path.exists(position):
                    os.makedirs(position )
                storage = open(position+'/'+file.name, 'wb+')
                for chunk in file.chunks():
                    storage.write(chunk)
                storage.close()
            return HttpResponse( '1')

dirs = []
@csrf_exempt
def getDirs(request):
    if request.method == 'POST':
        if 'paths' in request.POST:
            paths = request.POST['paths']
            # doSkwomething with pieFact here...
            dirs.append(paths)
            print(paths)
            return HttpResponse('success') # if everything is OK

    # nothing went well
    return HttpResponse('FAIL!!!!!')

def handle_uploaded_file(f, filename, user):
    path = '/home/mason/ether/static/accounts/'+ str(user.username) + '/' + str(filename)
    db_path = '/accounts/' + str(user.username) + '/' + str(filename)
    print("Path-----" + path)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    p = Profile.objects.get(user=user)
    print("path again--------" + path)
    fname, file_ext = os.path.splitext(path)
    print(file_ext)
    fi = File.objects.create(owner=p, name=str(filename), path=db_path, file_type=file_ext)
    fi.save()


@csrf_exempt
def foo(request):
    print("in fooooooo!")
    user = request.user
    files = request.FILES.getlist('file_field')
    print("FILES---------")
    for fi in files:
        print(fi.name)
        print("created obj")
        handle_uploaded_file(fi, fi.name, user)

    return HttpResponse('in fooo')

@csrf_exempt
def handle_upload(request):
    request.upload_handlers.insert(0, foo(request))

    files = request.FILES.getlist('file_field')
    print("handle----------")
    for f in files:
        print(files)
    return HttpResponse('success') # if everything is OK
