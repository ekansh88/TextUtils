# i made this file: ekansh
from django.http import HttpResponse
import os
from django.shortcuts import render

def about(request):
    return HttpResponse("<h1>about</h1>")

def displayTxt(request):
    f = open("/#1 textutils/textutils/one.txt", "r")
    return HttpResponse(f.read())

def exc1(request):
    s = '''<h1>Navigation</h1>
        <a href="https://www.facebook.com/"> Facebook </a> <br>
        <a href="https://www.flipkart.com/"> Flipkart </a> <br>
        <a href="https://www.hindustantimes.com/"> News </a> <br>
        <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)

def goToHomeLink():
    return HttpResponse("<a href='http://127.0.0.1:8000/'>HOME</a>")

def home(request):
    a = """
        <p>HOME</p>
        <button><a href="/analyze">analyze</a></button>
        <button><a href="/index">index</a></button>
        <button><a href="/removePunc">removePunc</a></button>
        <button><a href="/capatilizeFirst">capatilizeFirst</a></button>
        <button><a href="/spaceRemove">spaceRemove</a></button>
        <button><a href="/charCount">charCount</a></button>
        """
    return HttpResponse(a)
    # return HttpResponse("home")

def index(request):
    # params  = {"name":"ekansh", "place":"Pluton"}
    return render(request, "index.html")
    # return HttpResponse("index")


# def capatilizeFirst(request):
#     return HttpResponse("capatilizeFirst")
#
# def spaceRemove(request):
#     return HttpResponse("spaceRemove")
#
# def charCount(request):
#     return HttpResponse("charCount")

def removePunc(request):
    return HttpResponse(f"removePunc")


def analyze(request):
    djText = request.POST.get("text", "default")
    djRemovePunc = request.POST.get("removePunc", "off")
    djUpperCase = request.POST.get("upperCase", "off")
    djNewLineRemover = request.POST.get("newLineRemover", "off")

    # print(djText, "\n", djRemovePunc)
    res = djText
    if djRemovePunc=="on":
        tmp = ""
        punc = set(list('''!@#$%^&*()~`:"|{}[];'\/.,<>?/*-.'''))
        for i in res:
            if i not in punc:
                tmp += i
        res = tmp
    if djUpperCase=="on":
            res = res.upper()
    if djNewLineRemover=="on":
        tmp = ""
        for i in res:
            if i!="/n" or i!="/r":
                tmp += i
        res = tmp

    params = {"analyzed_text":res, "purpose":"Remove Puntuation"}
    return render(request, "analyze.html", params)