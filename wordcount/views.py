from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse('Hello')
    return render(request,'home.html')

def testpage(request):
    return HttpResponse('<h1>測試HTML TAG</h1>')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)        
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})

def about(request):
    #return HttpResponse('Hello')
    return render(request,'about.html')