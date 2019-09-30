# This is test file created by vishal.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('''<h1>hello Vishal</h1> <a href="https://www.w3schools.com">Visit W3Schools.com!</a>''')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepun', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    #analyzed = "djtext"
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for j in djtext:
            if j not in punctuations:
                analyzed = analyzed + j

        params = {'purpose': "Remove Punctuations", "analyzed_text": analyzed}
        return render(request,'analyze.html',params)
    elif(fullcaps == "on"):
        analyzed = ""
        for j in djtext:
            analyzed = analyzed + j.upper()
        params = {'purpose': "Remove Punctuations", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for j in djtext:
            if j != "\n" and j !="\r":
                analyzed = analyzed + j

        params = {'purpose': "Removed New line character", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for j,k in enumerate(djtext):
            if djtext[j] == " " and djtext[j+1] ==  " ":
                pass
            else:
                analyzed = analyzed + k
        params = {'purpose': "Remove extra space", "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
# def removepunc(request):
#     djtext= request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("Remove pun")
# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse('''"spaceremove" <a href="/">Back</a>''')
