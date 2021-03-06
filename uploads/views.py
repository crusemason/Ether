from django.shortcuts import render
from django.db import transaction
from django import template
import os.path
from os import path as ospath
import shutil
from django.db import transaction
from django.shortcuts import render_to_response
from django import template
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.template import Template
from django.http import HttpResponse
from django.http import JsonResponse
from .models import File, Folder, Photo
from accounts.models import Profile
from django.core.files import File as DjangoFile
from datetime import date
from datetime import datetime
from datetime import timedelta
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import time
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core import serializers

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo

from .forms import PhotoForm
from .models import Photo
import os
import pytz
import re

# Create your views here.
fdict = {}
dirs = []
nodupdirs = []
p = []
pieFact = None
filedic = {}
missinglist = []
#created = folder dict name is key value is folder id
created = {}

#list for all uploaded files successful or not
all_upload = []

#list for files successfully uploaded
s_upload = []


register = template.Library()

@register.filter()
def range(min=5):
    return range(min)

def getstorage(pro):
    storage = pro.storage
    storage = int(storage/1500000)
    return storage

@csrf_exempt
@login_required(login_url='/users/login/')
def home(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    storage = getstorage(pro)
    print(storage)
    image_list = File.objects.all()
    context = {"image_list":image_list, 'storage':storage}
    return render(request, 'home.html', context)

@login_required(login_url='/users/login/')
def recent(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    storage = getstorage(pro)
    image_list = File.objects.all()
    today_list = []
    week_list = []
    month_list = []
    year_list = []
    sep = ' '
    today = datetime.now()
    week = datetime.now() + timedelta(days=7)
    month = datetime.now() + timedelta(days=28)
    year = datetime.now() + timedelta(days=365)
    today = pytz.utc.localize(today)
    week = pytz.utc.localize(week)
    month = pytz.utc.localize(month)
    year = pytz.utc.localize(year)
    for image in image_list:
        print(image.modified)
        rest = image.modified
        #rest = pytz.utc.localize(rest)
        print(str(rest))
        if rest == today:
            today_list.append(image)
        elif rest <= week and rest > today:
            week_list.append(image)
        elif rest <= month and rest > week:
            month_list.append(image)
        elif rest > month:
            year_list.append(image)


    context = {"image_list":image_list, 'week_list':week_list, 'month_list':month_list, 'year_list':year_list, 'storage':storage}

    return render(request, 'recent.html', context)
@csrf_exempt
@login_required(login_url='/users/login/')
def mydrive(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    storage = getstorage(pro)
    image_list = File.objects.filter(owner=pro)
    folder_list = None
    if pro.gid != 0:
        g = Folder.objects.get(id=pro.gid)
        folder_list = Folder.objects.filter(parent=g)
    qa_list = []
    x = 0

    for image in image_list:
        if 'jpeg' or 'png' or 'jpg' in image.file_type:
            x = x + 1
            if x == 20:
                return render(request, 'my-drive.html', context)
            qa_list.append(image)
            context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list, 'storage':storage}


    context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list, 'storage':storage}
    return render(request, 'my-drive.html', context)

@csrf_exempt
@login_required(login_url='/users/login/')
def mydrivetable(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    storage = getstorage(pro)
    me = user.email
    image_list = File.objects.filter(owner=pro)
    folder_list = None
    if pro.gid != 0:
        g = Folder.objects.get(id=pro.gid)
        folder_list = Folder.objects.filter(parent=g)
    qa_list = []
    x = 0

    for image in image_list:
        if 'jpeg' or 'png' or 'jpg' in image.file_type:
            x = x + 1
            if x == 20:
                return render(request, 'my-drive-table.html', context)
            qa_list.append(image)
            context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list, 'me':me, 'storage':storage}


    context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list, 'me':me, 'storage':storage}
    return render(request, 'my-drive-table.html', context)

@csrf_exempt
@login_required(login_url='/users/login/')
def mydrivetableimagesearch(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    storage = getstorage(pro)
    me = user.email
    image_list = File.objects.filter(owner=pro)
    folder_list = None
    if pro.gid != 0:
        g = Folder.objects.get(id=pro.gid)
        folder_list = Folder.objects.filter(parent=g)
    qa_list = []
    x = 0

    for image in image_list:
        if 'jpeg' or 'png' or 'jpg' in image.file_type:
            x = x + 1
            if x == 20:
                return render(request, 'my-drive-table-imagesearch.html', context)
            context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list, 'me':me, 'storage':storage}


    context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list, 'me':me, 'storage':storage}
    return render(request, 'my-drive-table.html', context)





@csrf_exempt
@login_required(login_url='/users/login/')
def mydrivetrash(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    storage = getstorage(pro)
    image_list = File.objects.filter(owner=pro, trash=True)
    folder_list = None
    if pro.gid != 0:
        g = Folder.objects.get(id=pro.gid)
        folder_list = Folder.objects.filter(parent=g, trash=True)
    qa_list = []
    x = 0

    if(image_list):
        for image in image_list:
            if 'jpeg' or 'png' or 'jpg' in image.file_type:
                x = x + 1
                if x == 11:
                    return render(request, 'my-drive-trash.html', context)
                qa_list.append(image)
                if(len(image_list) == 0):
                    context = {'folder_list':folder_list}
                if(len(folder_list) == 0):
                    context = {'image_list':image_list}
                if(len(folder_list) != 0 and len(image_list) != 0):
                    context = {"image_list":image_list, 'folder_list':folder_list, 'storage':storage}

    if(len(image_list) == 0):
        context = {'folder_list':folder_list, 'storage':storage}
    if(folder_list):
        if(len(folder_list) == 0):
            context = {'image_list':image_list, 'storage':storage}
    if(folder_list and image_list):
        if(len(folder_list) != 0 and len(image_list) != 0):
            context = {"image_list":image_list, 'folder_list':folder_list, 'storage':storage}


    return render(request, 'my-drive-trash.html', context)

@csrf_exempt
@login_required(login_url='/users/login/')
def upload(request):
    firstfolder(request)

    if request.method == 'POST':

        dir=request.FILES
        dirlist=dir.getlist('files')
        pathlist=request.POST.getlist('paths')
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


def checkFolderUpload(path):
    if( ospath.exists(path) ):
        print("yes")
    else:
        return HttpResponse('fail') # if everything is NOT ok

    return

@csrf_exempt
@login_required(login_url='/users/login/')
def getDirs(request):
    if request.method == 'POST':
        if 'paths' in request.POST:
            paths = request.POST['paths']
            # doSkwomething with pieFact here...
            dirs.append(paths)
            print('paths-----------')
            print(paths)
            return HttpResponse('success') # if everything is OK

    # nothing went well
    return HttpResponse('FAIL!!!!!')

def handle_uploaded_file(f, filename, user, mypath):
    #create path for uploaded file
    #path = '/home/mason/ether/static/accounts/'+ str(user.email) + '/' + 'genesis/' + mypath + filename
    ##create path to store in the database
    #db_path = '/accounts/' + str(user.email) + '/' + 'genesis/' + mypath + filename
    ##write file to disk
    #with open(path, 'wb+') as destination:
        #for chunk in f.chunks():
            #destination.write(chunk)
        #checkFolderUpload(path)
        #print('DESTINATION-------------------------'+str(destination))
    ##create file in database
    #p = Profile.objects.get(user=user)
    #fname, file_ext = os.path.splitext(path)
    #fi = File.objects.create(owner=p, name=str(filename), path=db_path, file_type=file_ext)
    #filesize= os.path.getsize('/home/mason/ether/static'+fi.path)
    #print('fsize'+str(filesize))
    #p.storage = p.storage + filesize
    #p.save()
    #fi.size = str(filesize)
    #fi.save()
    #count = mypath.count('/')
    #if count == 1:
        #print('my path-----'+mypath)
        #mypath = mypath.replace('/','')
    #else:
        #print('my path-----'+mypath)
        #mypath = re.sub(".*/", "", mypath[:-1])
    #print('mypath-----'+mypath+' count='+str(count))
    #fi.save()
    #return fi
    print("handle upload file")
#

@csrf_exempt
@login_required(login_url='/users/login/')
def foo(request):
    #mylist = []
    #user = request.user
    #print(filedic)
    #pro = Profile.objects.get(user=user)
    #gf = Folder.objects.get(id=pro.gid)
    #if 'paths' in request.POST:
        #paths = request.POST['paths']
        ## doSkwomething with pieFact here...
#
    #print('path='+str(p))
    #files = request.FILES.getlist('file_field')
    #missedfiles = []
    #for fi in files:
        #if fi.name in filedic:
            #f0 = handle_uploaded_file(fi, fi.name, user, filedic[fi.name])
            #f0.save()
            #print('foopath='+filedic[fi.name])
            #temp = filedic[fi.name]
            #count = temp.count('/')
            #if count == 1:
                #print('foo path-----'+temp)
                #temp = temp.replace('/','')
                #print('p='+temp)
                #fdict.setdefault(temp, [])
                #fdict[temp].append(f0.id)
            #else:
                #print('foo path-----'+temp)
                #temp = re.sub(".*/", "", temp[:-1])
                #print('temp-----'+temp+' count='+str(count))
                #fdict.setdefault(temp, [])
                #fdict[temp].append(f0.id)
        #else:
            #missinglist.append(fi.name)
#
    #once = 0
    #capturenext = 0
    #counter = 0
#
#
    #for d in dirs:
        #print(d)
        #if(d in fdict):
            #print('fdict-----------'+str(fdict[d]))
            #mylist1 = []
            #for fd in fdict[d]:
                #print('fd='+str(fd))
                #mylist1.append(fd)
            #index = dirs.index(d)
            #print('index='+str(index))
            #if once == 0:
                #once = 1
                #f = Folder.objects.create(owner=pro, parent=gf, name=d, path=gf.path+d)
                #for my in mylist1:
                    #fi = File.objects.get(id=my)
                    #f.folderfiles.add(fi)
                    #f.save()
                #print('fname----------',f.name)
                #created.update({f.name:f.id})
                #mylist.append(d)
                #print(mylist[0])
#
            #if d in created:
                #pass
            #else:
                #print('fname----------',f.name)
                #print('mylist='+str(dirs[index-1]))
                #pid = created[dirs[index-1]]
                #print('parent id='+str(pid))
                #pf = Folder.objects.get(id=pid)
                #f = Folder.objects.create(owner=pro, parent=pf, name=d, path=pf.path+'/'+d)
                #print(fdict)
                #if  d in fdict:
                    #xx = fdict[d]
                    #print('xx-------'+str(xx))
                    #for x in xx:
                        #print('x='+str(x))
                        #filef = File.objects.get(id=x)
                        #f.folderfiles.add(filef)
                #created.update({f.name:f.id})
    #print(created)

    return HttpResponse('in fooo')

@csrf_exempt
@login_required(login_url='/users/login/')
def handle_upload(request):
    request.upload_handlers.insert(0, foo(request))

    #files = request.FILES.getlist('file_field')
    return HttpResponse('success') # if everything is OK

@login_required(login_url='/users/login/')
def trash(request, slug, pk):
    f = File.objects.get(pk=pk)
    if(f.trash == True):
        os.remove('/home/mason/ether/static'+f.path)
        f.delete()
        print("delete")
        print(f.path)
        image_list = File.objects.all()
        context = {"image_list":image_list}
        return render(request, 'home.html', context)
    f.trash = True
    f.save()
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

@login_required(login_url='/users/login/')
def trashfolder(request, slug, pk):
    f = Folder.objects.get(pk=pk)
    if(f.trash == True):
        os.remove('/home/mason/ether/static'+f.path)
        f.delete()
        print("delete")
        print(f.path)
        image_list = Folder.objects.all()
        context = {"image_list":image_list}
        return render(request, 'home.html', context)
    f.trash = True
    f.save()
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

def allTrash(request):
    image_list  = File.objects.all().filter(trash=True)
    folder_list  = Folder.objects.all()
    context = {"image_list":image_list, 'folder_list:':folder_list}
    return render(request, 'trash.html', context)

def allStarred(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    image_list = File.objects.filter(owner=pro)
    folder_list = None
    if pro.gid != 0:
        g = Folder.objects.get(id=pro.gid)
        folder_list = Folder.objects.filter(parent=g,starred=True)
    image_list  = File.objects.all().filter(starred=True)
    context = {"image_list":image_list, "folder_list":folder_list}
    return render(request, 'starred.html', context)

def star(request, slug, pk):
    f = File.objects.get(pk=pk)
    f.starred = True
    f.save()
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

def starfolder(request, slug, pk):
    f = Folder.objects.get(pk=pk)
    f.starred = True
    f.save()
    image_list = Folder.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

def removestar(request, slug, pk):
    f = File.objects.get(pk=pk)
    f.starred = False
    f.save()
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

@csrf_exempt
def firstfolder(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    path = '/home/mason/ether/static/accounts/'+ str(user)
    print(pro.gid)
    if pro.gid == 0:
        os.chdir(path)
        os.mkdir('genesis')
        path += '/genesis/'
        g = Folder.objects.create(path = path, owner=pro, name='genesis')

        os.chdir(path)
        f = Folder.objects.create(path = path+foldername, owner=pro, name=foldername, parent=g)
        os.mkdir(foldername)
        g.children.add(f)
        g.save()

        pro.gid = g.id
        pro.save()

        return 1
    else:

        return 0


@csrf_exempt
def rootfolder(request):
    foldername = request.POST.get('newfolder-q','')
    print(foldername)
    user = request.user
    pro = Profile.objects.get(user=user)
    path = '/home/mason/ether/static/accounts/'+ str(user)
    print(pro.gid)
    if pro.gid == 0:
        os.chdir(path)
        os.mkdir('genesis')
        path += '/genesis/'
        g = Folder.objects.create(path = path, owner=pro, name='genesis')

        os.chdir(path)
        f = Folder.objects.create(path = path+foldername, owner=pro, name=foldername, parent=g)
        os.mkdir(foldername)
        g.children.add(f)
        g.save()

        pro.gid = g.id
        pro.save()
    else:
        g = Folder.objects.get(id=pro.gid)
        print('g path  ' + g.path)
        f = Folder.objects.create(path = g.path+foldername, owner=pro, name=foldername, parent=g)
        os.chdir(g.path)
        os.mkdir(foldername)
        g.children.add(f)
        g.save()

        print('gid not 0')

    print(user)
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

def subfolder(request, pk):
    request.session['fid'] = pk
    f = Folder.objects.get(id=pk)
    folder_list = Folder.objects.filter(parent=f)
    image_list = f.folderfiles.all()
    context = {'folder_list':folder_list, 'image_list':image_list, 'parent':f}
    return render(request, 'subfolder.html', context)

@csrf_exempt
def makesubfolder(request):
    pf = Folder.objects.get(id=request.session['fid'])
    user = request.user
    pro = Profile.objects.get(user=user)
    foldername = request.POST.get('newfolder-q','')
    sf = Folder.objects.create(parent=pf, owner=pro, name=foldername, path=pf.path+'/'+foldername)
    os.chdir(pf.path)
    os.mkdir(foldername)
    pf.children.add(sf)
    pf.save()
    folder_list = Folder.objects.filter(parent=pf)
    context = {'folder_list':folder_list, 'parent':pf}
    return render(request, 'subfolder.html', context)


@csrf_exempt
def uploadfileat(request):
    firstfolder(request)
    pf = Folder.objects.get(id=request.session['fid'])
    user = request.user
    pro = Profile.objects.get(user=user)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        f = File.objects.create(owner=pro, name=myfile.name, folder=pf, path=pf.path+'/'+myfile.name)
        fs = FileSystemStorage(pf.path+'/')
        fs.save(myfile.name,myfile)
    folder_list = Folder.objects.filter(parent=pf)
    image_list = File.objects.filter(folder=pf)
    context = {'folder_list':folder_list}
    return render(request, 'subfolder.html', context)

def validate_upload(request):
    file_field = request.POST.get('file_field', None)
    data = {
        'file_field':file_field
    }
    return JsonResponse(data)

def makedirs(dirs):
    print('in make dirs---------')
    d.split(os.sep)
    print(d)


#gets called for every file and folder uploaded
@csrf_exempt
@transaction.atomic
def my_view_that_updates_pieFact(request):
    #get the user uploading a folder
    user = request.user
    print("Folder upload by " + str(user))

    #get the profile for that user
    pro = Profile.objects.get(user=user)

    #get profiles genesis folder id
    gf = Folder.objects.get(id=pro.gid)
    f = Folder()
    if request.method == 'POST':
        #if pieFact is in POST then a user has uploaded a folder
        #pieFact contains the path of all uploaded files and folders
        if 'pieFact' in request.POST:
            pieFact = request.POST['pieFact']

            #parse path
            temp = pieFact
            print("temp-----",temp)

            #temp is uploaded folder topology
            p = temp.split('/')[-1]
            temp = temp.replace(p,'')
            print("temp-----",temp)

            #change directoy to genesis folder
            os.chdir('/home/mason/ether/static/accounts/'+str(pro.user)+'/genesis/')

            #make uploaded folders on the server
            print("making dirs")
            if not os.path.exists(temp):
                os.makedirs(temp)

            #print('p----------'+str(p))
            pieFact = pieFact.split(os.sep)
            print("pieFact=%s",pieFact)
            #get filename from path
            fname = pieFact[-1]
            print("fname=%s",fname)

            #filedic contains a dict of files where the filename is the key
            # and the path is the value
            filedic.update({fname:temp})
            print('filedic'+str(filedic))

            #get all folders from path
            for pie in pieFact[:-1]:
                dirs.append(pie)
            #remove any duplicates from dirs
            for d in dirs:
                print("d-------- %s",d)

            ## doSomething with pieFact here...
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')

def download(request, slug, pk):
    f = File.objects.get(id=pk)
    path = '/home/mason/ether/static'
    path += f.path
    print('fromdownloaditem'+path)
    f0 = open(path, 'rb')
    myfile = DjangoFile(f0)
    response = HttpResponse(myfile)
    response['Content-Disposition'] = 'attachment; filename=' + f.name
    return response

def downloadfolder(request, slug, pk):
    f = Folder.objects.get(id=pk)
    print('fromdownloaditem'+f.path)
    shutil.make_archive(f.path, 'zip', f.path)
    f0 = open(f.path+'.zip', 'rb')
    myfile = DjangoFile(f0)
    response = HttpResponse(myfile)
    response['Content-Disposition'] = 'attachment; filename=' + f.name+'.zip'
    return response





class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = File.objects.all()
        return render(self.request, 'uploads/progress_bar_upload/index.html', {'photos': photos_list})

    def post(self, request):
        time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = PhotoForm(self.request.POST, self.request.FILES)
        user = request.user
        pro = Profile.objects.get(user=user)
        form.instance.owner = pro

        if form.is_valid():
            File = form.save()
            name = File.file.name
            File.name = name
            File.save()
            print(File)
            data = {'is_valid': True, 'name': File.file.name, 'url': File.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            photo.owner
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))


@csrf_exempt
def searchajax(request):
    searchq = request.GET.get('searchq', None)
    if request.method == "POST":
        searchq = request.POST['searchq']
    print('in search')
    print(searchq)
    f_json = False
    if(File.objects.filter(name__contains=searchq).exists()):
            f = File.objects.filter(name__contains=searchq)

    data = {
        'is_taken': f_json
    }
    return render_to_response('ajax_search.html', {'files':f})
