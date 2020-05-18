from django.contrib import admin

from .models import Planet, Sith, Recruit, Answers, TestShadowArm


admin.site.register(Answers)
admin.site.register(Recruit)
admin.site.register(Planet)
admin.site.register(Sith)
admin.site.register(TestShadowArm)
# Register your models here.
