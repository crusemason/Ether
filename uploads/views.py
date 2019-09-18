from django.shortcuts import render
from django.db import transaction
from django import template
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.template import Template
from django.http import HttpResponse
from django.http import JsonResponse
from .models import File, Folder
from accounts.models import Profile
from django.core.files import File as DjangoFile
from datetime import date
from datetime import datetime
from datetime import timedelta
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import os
import pytz
import re

# Create your views here.
fdict = {}
dirs = []
p = []
pieFact = None
filedic = {}
missinglist = []
#created = folder dict name is key value is folder id
created = {}

@csrf_exempt
def home(request):
    image_list = File.objects.all()
    context = {"image_list":image_list}
    return render(request, 'home.html', context)

def recent(request):
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


    context = {"image_list":image_list, 'week_list':week_list, 'month_list':month_list, 'year_list':year_list}

    return render(request, 'recent.html', context)


@csrf_exempt
def mydrive(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    image_list = File.objects.all()
    folder_list = None
    if pro.gid != 0:
        g = Folder.objects.get(id=pro.gid)
        folder_list = Folder.objects.filter(parent=g)
    qa_list = []
    x = 0

    for image in image_list:
        if 'jpeg' or 'png' or 'jpg' in image.file_type:
            x = x + 1
            if x == 8:
                return render(request, 'my-drive.html', context)
            qa_list.append(image)
            context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list}


    context = {"image_list":image_list, "qa_list":qa_list, 'folder_list':folder_list}
    return render(request, 'my-drive.html', context)

@csrf_exempt
def upload(request):

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

dirs = []
@csrf_exempt
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
    path = '/home/mason/ether/static/accounts/'+ str(user.username) + '/' + 'genesis/' + mypath + filename
    db_path = '/accounts/' + str(user.username) + '/' + 'genesis/' + mypath + filename
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    p = Profile.objects.get(user=user)
    fname, file_ext = os.path.splitext(path)
    fi = File.objects.create(owner=p, name=str(filename), path=db_path, file_type=file_ext)
    count = mypath.count('/')
    if count == 1:
        print('my path-----'+mypath)
        mypath = mypath.replace('/','')
    else:
        print('my path-----'+mypath)
        mypath = re.sub(".*/", "", mypath[:-1])
    print('mypath-----'+mypath+' count='+str(count))
    fi.save()
    return fi


@csrf_exempt
def foo(request):
    mylist = []
    user = request.user
    print(filedic)
    pro = Profile.objects.get(user=user)
    gf = Folder.objects.get(id=pro.gid)
    if 'paths' in request.POST:
        paths = request.POST['paths']
        # doSkwomething with pieFact here...

    print('path='+str(p))
    files = request.FILES.getlist('file_field')
    missedfiles = []
    for fi in files:
        if fi.name in filedic:
            f0 = handle_uploaded_file(fi, fi.name, user, filedic[fi.name])
            f0.save()
            print('foopath='+filedic[fi.name])
            temp = filedic[fi.name]
            count = temp.count('/')
            if count == 1:
                print('foo path-----'+temp)
                temp = temp.replace('/','')
                print('p='+temp)
                fdict.setdefault(temp, [])
                fdict[temp].append(f0.id)
            else:
                print('foo path-----'+temp)
                temp = re.sub(".*/", "", temp[:-1])
                print('temp-----'+temp+' count='+str(count))
                fdict.setdefault(temp, [])
                fdict[temp].append(f0.id)
        else:
            missinglist.append(fi.name)

    once = 0
    capturenext = 0
    counter = 0


    for d in dirs:
        print(d)
        print('fdict-----------'+str(fdict[d]))
        mylist1 = []
        for fd in fdict[d]:
            print('fd='+str(fd))
            mylist1.append(fd)
        index = dirs.index(d)
        print('index='+str(index))
        if once == 0:
            once = 1
            f = Folder.objects.create(owner=pro, parent=gf, name=d, path=gf.path+d)
            for my in mylist1:
                fi = File.objects.get(id=my)
                f.folderfiles.add(fi)
                f.save()
            print('fname----------',f.name)
            created.update({f.name:f.id})
            mylist.append(d)
            print(mylist[0])

        if d in created:
            pass
        else:
            print('fname----------',f.name)
            print('mylist='+str(dirs[index-1]))
            pid = created[dirs[index-1]]
            print('parent id='+str(pid))
            pf = Folder.objects.get(id=pid)
            f = Folder.objects.create(owner=pro, parent=pf, name=d, path=pf.path+'/'+d)
            print(fdict)
            if  d in fdict:
                xx = fdict[d]
                print('xx-------'+str(xx))
                for x in xx:
                    print('x='+str(x))
                    filef = File.objects.get(id=x)
                    f.folderfiles.add(filef)
            created.update({f.name:f.id})
    print(created)

    return HttpResponse('in fooo')

@csrf_exempt
def handle_upload(request):
    request.upload_handlers.insert(0, foo(request))

    files = request.FILES.getlist('file_field')
    return HttpResponse('success') # if everything is OK

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

def allTrash(request):
    image_list  = File.objects.all().filter(trash=True)
    context = {"image_list":image_list}
    return render(request, 'trash.html', context)

def allStarred(request):
    image_list  = File.objects.all().filter(starred=True)
    context = {"image_list":image_list}
    return render(request, 'starred.html', context)

def star(request, slug, pk):
    f = File.objects.get(pk=pk)
    f.starred = True
    f.save()
    image_list = File.objects.all()
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
    context = {'folder_list':folder_list, 'image_list':image_list}
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
    context = {'folder_list':folder_list}
    return render(request, 'subfolder.html', context)


@csrf_exempt
def uploadfileat(request):
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



@csrf_exempt
def my_view_that_updates_pieFact(request):
    user = request.user
    pro = Profile.objects.get(user=user)
    gf = Folder.objects.get(id=pro.gid)
    f = Folder()
    if request.method == 'POST':
        if 'pieFact' in request.POST:
            pieFact = request.POST['pieFact']
            temp = pieFact
            p = temp.split('/')[-1]
            temp = temp.replace(p,'')
            os.chdir('/home/mason/ether/static/accounts/admon/genesis/')
            if not os.path.exists(temp):
                os.makedirs(temp)

            print('p----------'+str(p))
            pieFact = pieFact.split(os.sep)
            fname = pieFact[-1]
            print('filedic'+str(filedic))
            filedic.update({fname:temp})
            for pie in pieFact[:-1]:
                dirs.append(pie)


            # doSomething with pieFact here...
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

