# Generated by Django 3.0.6 on 2020-05-17 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_planet', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestShadowArm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_question', models.CharField(max_length=200)),
                ('second_question', models.CharField(max_length=200)),
                ('third_question', models.CharField(max_length=200)),
                ('ordens_planet', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='system.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sith', models.CharField(max_length=200)),
                ('planet_sith', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='system.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_recruit', models.CharField(max_length=200)),
                ('age_recruit', models.IntegerField(default=0)),
                ('email_recruit', models.CharField(max_length=200)),
                ('planet_recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Planet')),
                ('teacher_recruit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='system.Sith')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_question', models.CharField(default=None, max_length=200)),
                ('second_question', models.CharField(default=None, max_length=200)),
                ('third_question', models.CharField(default=None, max_length=200)),
                ('name_recruit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='system.Recruit')),
            ],
        ),
    ]
