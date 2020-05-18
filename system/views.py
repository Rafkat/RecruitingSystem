from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Recruit, Sith, Planet, TestShadowArm, Answer


class ChooseSide(generic.TemplateView):
    template_name = 'system/side.html'


class CreateRecruit(generic.CreateView):
    model = Recruit
    fields = ['name', 'age', 'email', 'planet']
    template_name = "system/recruitform.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_planet'] = Planet.objects.order_by('name')
        return context

    def get_success_url(self):
        return reverse_lazy('TestRecruit', kwargs={'id': self.object.id})


class SithSide(generic.ListView):
    template_name = 'system/sithform.html'
    context_object_name = 'siths_list'
    queryset = Sith.objects.only('name')


class TestRecruit(generic.CreateView):
    model = Answer
    fields = ['first_question', 'second_question', 'third_question', 'name_recruit']
    success_url = reverse_lazy('ThankPage')
    template_name = "system/recruitstest.html"

    def get_context_data(self, **kwargs):
        recruits_planet = Recruit.objects.get(id=self.kwargs.get('id')).planet
        context = super().get_context_data(**kwargs)
        context['name_recruit'] = Recruit.objects.get(id=self.kwargs.get('id'))
        context['first_question'] = TestShadowArm.objects.get(ordens_planet=recruits_planet).first_question
        context['second_question'] = TestShadowArm.objects.get(ordens_planet=recruits_planet).second_question
        context['third_question'] = TestShadowArm.objects.get(ordens_planet=recruits_planet).third_question
        return context


class ThankPage(generic.TemplateView):
    template_name = 'system/thankpage.html'


class RecruitList(generic.ListView):
    model = Recruit
    template_name = 'system/recruitlist.html'
    context_object_name = 'recruits_list'
    queryset = Recruit.objects.filter(teacher=None)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['sith_id'] = self.request.GET.get('name_sith')
        return context


class AnswerList(generic.DetailView):
    model = Answer
    template_name = 'system/answerlist.html'
    context_object_name = 'answer'

    def get_object(self, queryset=None):
        answer = Answer.objects.get(name_recruit=self.kwargs.get('id'))
        return answer

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['sith_id'] = self.request.GET.get('sith_id')
        return context


class ChooseRecruit(generic.UpdateView):
    model = Recruit
    pk_url_kwarg = 'id'
    fields = ['teacher']
    success_url = reverse_lazy('RecruitList')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['recruit_list'] = Recruit.

# def index(request):
#    return HttpResponse("Hello,world. You're at the system.")
# Create your views here.
