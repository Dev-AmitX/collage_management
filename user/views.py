from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def index1(request):
    data=tbl_notice.objects.all().order_by('-id')[0:4]
    data1=tbl_feedback.objects.all().order_by('-id')[0:6]
    data2=tbl_event.objects.all().order_by('-id')[0:4]
    data3=tbl_slider.objects.all().order_by('id')
    md={'ndata':data,'fdata':data1,'edata':data2,'sdata':data3}
    return render(request,'index1.html',md)

def about(request):
    return render(request,'about.html')

def contact(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('subject')
        e=request.POST.get('msg')
        contactus(Name=a,Email=b,Mobile=c,Subject=d,Message=e).save()
        return HttpResponse("<script>alert('Data Save Successful');location.href='/contact/'</script>")

       #mydict={"name":a,"email":b,"mobile":c,"subject":d,"message":e}

    return render(request,'contact.html',mydict)

def courses(request):
    data=tbl_courses.objects.all().order_by('-id')
    md={'cdata':data}
    return render(request,'courses.html',md)

def faculty(request):
    data=tbl_faculty.objects.all().order_by('id')
    md={'fdata':data}
    return render(request,'faculty.html',md)

def feedback(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Picture=request.FILES['fu']
        Message=request.POST.get('message')
        tbl_feedback(name=Name,feedback=Message,picture=Picture).save()
        return HttpResponse("<script>alert('Thanks for your valuable feedback');location.href='/feedback/'</script>")

    return render(request,'feedback.html')

def gallery(request):
    data=tbl_gallery.objects.all().order_by('-id')[0:21]
    mydict={'gdata':data}
    return render(request,'gallery.html',mydict)

def infra(request):
    data=tbl_infra.objects.all().order_by('-id')
    md={'idata':data}
    return render(request,'infra.html',md)

def recruiters(request):
    data = tbl_recruiter.objects.all().order_by('-id')
    md = {'gdata': data}
    return render(request,'recruiters.html',md)

def alumny(request):
    data=tbl_alumni.objects.all().order_by('-id')
    ad={'adata':data}
    return render(request,'alumny.html',ad)

def primsg(request):
    return render(request,'primsg.html')