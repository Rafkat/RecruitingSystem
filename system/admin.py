from django.contrib import admin

from .models import Planet, Sith, Recruit, Answer, TestShadowArm

admin.site.register(Answer)
admin.site.register(Planet)
admin.site.register(Sith)
admin.site.register(TestShadowArm)
# Register your models here.
