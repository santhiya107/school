from django import forms
from.models import *

class Questionform(forms.ModelForm):
    class Meta:
        model = Question
        fields ="__all__"


class Answerform(forms.ModelForm):
    class Meta:
        model = Answers
        fields ="__all__"
        exclude = ['question']

class Chapterform(forms.ModelForm):
    class Meta:
        model = Chapter
        fields ="__all__"

class Subjectform(forms.ModelForm):
    class Meta:
        model = Subject
        fields ="__all__"

    
class grade_form(forms.ModelForm):
    
    class Meta:
        model = Grade
        fields = '__all__'

class subject_form(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields = '__all__'

class chapter_form(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'
        
class chapterlist_form(forms.Form):
    grade= forms.CharField(max_length=14)
    subject= forms.CharField(max_length=20)
        
class subjectlist_form(forms.Form):
    grade= forms.CharField(max_length=14)
    
      
class questionlist_form(forms.Form):
    grade= forms.CharField(max_length=14)
    subject= forms.CharField(max_length=20)
    no_of_questions= forms.CharField(max_length=20)

    
     
class question_form(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
      
    
 
    
class answer_form(forms.ModelForm):
    ans=question_form
    class Meta:
        model = Answers
        fields = '__all__'
        exclude=['question']
