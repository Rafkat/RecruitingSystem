from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Recruit, Sith, Planet, TestShadowArm, Answers


class ChooseSide(generic.TemplateView):
    template_name = 'system/side.html'


class NewRecruit(generic.TemplateView):
    template_name = "system/recruitform.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_planet'] = Planet.objects.order_by('name_planet')
        return context


class SithSide(generic.TemplateView):
    template_name = 'system/sithform.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['siths_list'] = Sith.objects.order_by('name_sith')
        return context


class SaveRecruit(generic.CreateView):
    model = Recruit
    fields = ['name_recruit', 'age_recruit', 'email_recruit', 'planet_recruit']
    success_url = reverse_lazy('TestRecruit')


class TestRecruit(generic.TemplateView):
    template_name = "system/recruitstest.html"

    def get_context_data(self, **kwargs):
        recruits_planet = Recruit.objects.last().planet_recruit
        context = super().get_context_data(**kwargs)
        # context['name_recruit'] = Recruit.objects.last().name_recruit
        context['first_question'] = TestShadowArm.objects.get(ordens_planet=recruits_planet).first_question
        context['second_question'] = TestShadowArm.objects.get(ordens_planet=recruits_planet).second_question
        context['third_question'] = TestShadowArm.objects.get(ordens_planet=recruits_planet).third_question
        return context


class SaveTest(generic.CreateView):
    model = Answers
    # name_recruit = Recruit.objects.last().name_recruit
    fields = ['first_question', 'second_question', 'third_question']
    success_url = reverse_lazy('ThankPage')


class ThankPage(generic.TemplateView):
    template_name = 'system/thankpage.html'


class RecruitList(generic.ListView):
    model = Recruit
    template_name = 'system/recruitlist.html'
    context_object_name = 'recruits_list'

    #def get_context_data(self, *, object_list=None, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['recruit_list'] = Recruit.

# def index(request):
#    return HttpResponse("Hello,world. You're at the system.")
# Create your views here.
