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
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)
    planet = models.ForeignKey(Planet, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recruit(models.Model):
    teacher = models.ForeignKey(Sith, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TestShadowArm(models.Model):
    ordens_planet = models.ForeignKey(Planet, default=None, on_delete=models.CASCADE)
    first_question = models.CharField(max_length=200)
    second_question = models.CharField(max_length=200)
    third_question = models.CharField(max_length=200)

    def __str__(self):
        return str(self.ordens_planet)


class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)

    first_question = models.CharField(default=None, max_length=200)
    second_question = models.CharField(default=None, max_length=200)
    third_question = models.CharField(default=None, max_length=200)

