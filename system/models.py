from django.db import models


class NewRecruit(models.Manager):
    def create_recruit(self, name_recruit,
                       age_recruit,
                       planet_recruit,
                       email_recruit):
        newrecruit = self.create(name_recruit=name_recruit,
                                 age_recruit=age_recruit,
                                 planet_recruit=planet_recruit,
                                 email_recruit=email_recruit)
        return newrecruit


class Planet(models.Model):
    name_planet = models.CharField(max_length=200)

    def __str__(self):
        return self.name_planet


class Sith(models.Model):
    name_sith = models.CharField(max_length=200, unique=True)
    planet_sith = models.ForeignKey(Planet, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_sith


class Recruit(models.Model):
    teacher_recruit = models.ForeignKey(Sith, null=True, on_delete=models.CASCADE)
    name_recruit = models.CharField(max_length=200)
    age_recruit = models.IntegerField(default=0)
    email_recruit = models.CharField(max_length=200)
    planet_recruit = models.ForeignKey(Planet,
                                       on_delete=models.CASCADE)

    def __str__(self):
        return self.name_recruit


class TestShadowArm(models.Model):
    ordens_planet = models.ForeignKey(Planet, default=None, on_delete=models.CASCADE)
    first_question = models.CharField(max_length=200)
    second_question = models.CharField(max_length=200)
    third_question = models.CharField(max_length=200)

    def __str__(self):
       return str(self.ordens_planet)


class Answers(models.Model):
    name_recruit = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
    # question = models.ForeignKey(TestShadowArm, on_delete=models.CASCADE)

    first_question = models.CharField(default=None, max_length=200)
    second_question = models.CharField(default=None, max_length=200)
    third_question = models.CharField(default=None, max_length=200)
    # second_answer_text = models.CharField(max_length=200)
    # third_answer_text = models.CharField(max_length=200)

    # def __str__(self):
    #    return self.name_recruit
# Create your models here.
