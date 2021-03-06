from dataclasses import field
from random import choices
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model  = Article
        fields = '__all__'



# class ArticleForm(forms.Form):
#     REGION_A = "sl"
#     REGION_B = "dj"
#     REGION_C = "gj"
#     REGION_D = "gm"
#     REGION_E = "bu"
#     REGIONS_CHOICES = [
#         (REGION_A, "서울"),
#         (REGION_B, "대전"),
#         (REGION_C, "광주"),
#         (REGION_D, "구미"),
#         (REGION_E, "부산")
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(widget=forms.Select, choices=REGIONS_CHOICES)