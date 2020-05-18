from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChooseSide.as_view(), name='ChooseSide'),
    path('sithside/', views.SithSide.as_view(), name='SithSide'),
    path('recruit/', views.CreateRecruit.as_view(), name='Recruit'),
    path('testrecruit/<int:id>/', views.TestRecruit.as_view(), name='TestRecruit'),
    path('thankpage/', views.ThankPage.as_view(), name='ThankPage'),
    path('recruitlist/', views.RecruitList.as_view(), name='RecruitList'),
    path('answerlist/<int:id>/', views.AnswerList.as_view(), name='AnswerList'),
    path('chooserecruit/<int:id>/', views.ChooseRecruit.as_view(), name='ChooseRecruit'),
]
