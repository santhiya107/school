from django.urls import path
from.FrontendViews import *


urlpatterns=[

    path('academics/',gradeview,name='academics'),   
    path('question',questionview,name='question'),
    path('question-paper',question_paperview,name='question_paper'),
    
    path('subject-list',subjectlist,name='subjectlist'),
    path('chapterlist',chapterlistview,name='chapterlist'),
    path('subject',subjectcrud,name='subjectcrud'),
    path('chapter',chaptercrud,name='chaptercrud'),
    path('questions',questioncreationview,name='questioncreationview'),
    path('queslist',questionlistview,name='questionlistview')
]