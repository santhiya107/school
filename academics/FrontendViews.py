from urllib import response

from accounts.forms import login_form
from . forms import *
from django.shortcuts import render,redirect
from .models import *
import requests
import json


def simple(request):      
    form=login_form()
    return render(request,'accounts/login.html',{'form':form})

def gradeview(request): 
    form=grade_form()  
    return render(request,'academics/grade.html',{'form':form})

def questioncreationview(request): 
    form=question_form()
    form1=answer_form()      
    return render(request,'academics/question.html',{'form':form,'form1':form1})

 
def chapterlistview(request):
    form=chapterlist_form()
    return render(request,'academics/chapterlist.html',{'form':form})

def questionlistview(request):  
    form=questionlist_form()
    return render(request,'academics/questionlist.html',{'form':form})

def chaptercrud(request):  
    form= chapter_form()
    return render(request,'academics/chapters.html',{'form':form})

def subjectcrud(request):   
    form= subject_form()
    return render(request,'academics/subjectcreate.html',{'form':form})

def questionview(request):    
    questionform = Questionform()
    answerform = Answerform()
    return render(request,'academics/questionandanswers.html',{'answerform':answerform,'questionform':questionform})

def question_paperview(request):
     return render(request,'academics/question_paper.html')

def subjectlist(request):
    form=grade_form()  
    return render(request,'academics/gradelist.html',{'form':form})
    
 





    
