from django.urls import path
from.FrontendViews import *


urlpatterns=[
   
    
    path('grade',gradeview,name='gradeview'),
    path('chaplist',chapterlistview,name='chapterlistview'),
    path('subject',subjectcrud,name='subjectcrud'),
    path('chapter',chaptercrud,name='chaptercrud'),
    path('questions',questioncreationview,name='questioncreationview'),
    path('queslist',questionlistview,name='questionlistview'),
    path('ques',questionview,name='questionview'),
    path('quespaper',question_paperview,name='question_paperview')
]