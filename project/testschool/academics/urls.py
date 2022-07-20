from django.urls import path
from .views import ( 
    GradeView, 
    SubjectCreateView,
    SubjectEditView,
    ChaptersCreateView,
    ChapterEditView,
    ChapterListView,
    SubjectListView,
    QuestionCreateView,
    QuestionEditView,
    QuestionList,
    QuestionPaperView,

)
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('subjects/',SubjectCreateView.as_view()),
    path('grades/',GradeView.as_view()),
    path('chapters/',ChaptersCreateView.as_view()),
    path('subjects/<int:pk>/',SubjectEditView.as_view()),
    path('chapters/<int:pk>/',ChapterEditView.as_view()),
    path('chapter-list/',csrf_exempt(ChapterListView.as_view())),
    path('subject-list/',SubjectListView.as_view()),
    path('question/',QuestionCreateView.as_view()),
    path('question/<int:pk>/',QuestionEditView.as_view()),
    path('question-paper/',QuestionList.as_view()),
    path('question-paper/<int:pk>/',QuestionPaperView.as_view()),

]