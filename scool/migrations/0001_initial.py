# Generated by Django 5.0.3 on 2024-03-18 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('an', 'Android'), ('fr', 'FrontEnd')], default='', max_length=25, verbose_name='Наименование')),
                ('course_num', models.SmallIntegerField(default=0, verbose_name='Номер курса')),
                ('start_date', models.DateField(null=True, verbose_name='Начало курса')),
                ('end_date', models.DateField(null=True, verbose_name='Окончание курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'unique_together': {('name', 'course_num')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('first_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('age', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(99)], verbose_name='Возраст')),
                ('course', models.ManyToManyField(blank=True, to='scool.course', verbose_name='Посещаемые курсы')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
                'db_table': 'students',
                'indexes': [models.Index(fields=['first_name'], name='students_first_n_73f9e9_idx')],
            },
        ),
    ]
