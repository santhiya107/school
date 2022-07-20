from urllib import response
from . forms import *
from django.shortcuts import render,redirect
from .models import *
import requests
import json



def gradeview(request): 
    # form=grade_form()  
    # response=requests.get('https://schooltestproject.herokuapp.com/academics/grades/')
    # grade=response.json()    
    # return render(request,'academics/grade.html',{'grade':grade,'form':form})
    gradeform = grade_form
    subjectform = Subjectform
    chapterform = Chapterform
    return render(request,'academics/grade-subject-chapter.html',{'gradeform':gradeform,'subjectform':subjectform,'chapterform':chapterform})


def questioncreationview(request): 
    form=question_form()
    form1=answer_form()  
    response=requests.get('https://schooltestproject.herokuapp.com/academics/question/')
    question=response.json()   
    return render(request,'academics/question.html',{'question':question,'form':form,'form1':form1})

 
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
    form=questionlist_form()
    list_form = chapterlist_form()
    return render(request,'academics/question_paper.html',{'form':form,'list_form':list_form})
 





    
