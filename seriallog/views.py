from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Serial_Error_keywords
from .services import yield_huge_files, ErrorKeyWords
from django.contrib.auth.decorators import login_required


def  home(request):
    if request.method=='POST' and request.FILES['seriallog']:
        seriallog_file = request.FILES['seriallog']
        #return render(request,'seriallog/home.html',context={'title':'Serial Log Analyzer', 'analysis':['Error in /etc/fstab', 'Error in Network Configuration. Hence Primary interface is not up. Retrying Silently']})
        return render(request,'seriallog/home.html',context={'title':'Serial Log Analyzer', 'analysis':yield_huge_files(seriallog_file)})
    return render(request,'seriallog/home.html',context={'title':'Serial Log Analyzer'})

@login_required(login_url='common-login')
def seriallog_error(request):
    if request.method=='POST':
        if request.POST.get("issue") and request.POST.get("cause"):
            issue = request.POST.get("issue"); cause = request.POST.get("cause")
            print(issue,cause)
            ErrorKeyWords.update_error_keywords([{'issue':issue, 'cause':cause}])
        return redirect('seriallog-home')               
    return render(request,'seriallog/seriallog_error.html')        
