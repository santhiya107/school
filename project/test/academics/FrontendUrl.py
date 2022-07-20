from django.urls import path
from.FrontendViews import *


urlpatterns=[
   
    
    path('academics/',gradeview,name='gradeview'),
    path('chapterlist',chapterlistview,name='chapterlistview'),
    path('subject',subjectcrud,name='subjectcrud'),
    path('chapter',chaptercrud,name='chaptercrud'),
    path('questions',questionview,name='questioncreationview'),
    path('queslist',questionlistview,name='questionlistview'),
    path('ques',questionview,name='questionview'),
    path('question-paper',question_paperview,name='question_paperview')
]