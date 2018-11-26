
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{'name': 'Uniyal'})

def count(request):
    text = request.GET['text']
    wordList = text.split()
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    return render(request,'count.html', {'textbox':text, 'wordCount':len(wordList), 'wordDictionary':wordDictionary})

def aboutus(request):
    return render(request,'aboutus.html',{'key':'This is about us'})
