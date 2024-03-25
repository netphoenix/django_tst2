from django.db import models
from django.urls import reverse
from django.core.validators import (
    MinValueValidator, 
    MaxValueValidator)

class Person(models.Model):
    last_name = models.CharField(
            max_length=25,
            verbose_name = 'Имя'
            # null=False,
            # blank = False, 
            # db_column
            # editable 
            # error_messages null, blank, invalid, unique_for_date
            # uniqeu = True
            # unique_for_date = DataColumn
            )
    first_name = models.CharField(
            max_length=25,
            verbose_name = 'Фамилия')
    age = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(12), MaxValueValidator(99)],
        verbose_name = 'Возраст')
    course = models.ManyToManyField(
            'Course', 
            blank=True,
            verbose_name = 'Посещаемые курсы')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        blank=True,
        verbose_name='Фото')
    
    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.age}'
    
    def get_absolute_url(self):
        return reverse('person', kwargs={'id': self.pk})

    class Meta:
        indexes= [models.Index(fields=['first_name'])]
        # ordering = ['first_name']
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
        db_table = 'students'
        # absrtract = True


class Course(models.Model):
    langs = [
        ("py","Python"),
        ("js","JavaScript"),
        ("an","Android"),
        ('fr','FrontEnd')
    ]    
    name = models.CharField(
        max_length=25, 
        choices=langs,
        default='',
        blank = False,
        verbose_name = 'Наименование')
    course_num = models.SmallIntegerField(
            default=0,
            verbose_name = 'Номер курса')
    start_date = models.DateField(verbose_name = 'Начало курса', null=True)
    end_date = models.DateField(verbose_name = 'Окончание курса', null=True)
    description = models.TextField(blank=True, verbose_name = 'Описание')

    def __str__(self) -> str:
        return f'{self.get_name_display()}-{self.course_num}'
    
    def get_absolute_url(self):
        return reverse('editcourse', kwargs={'id': self.pk})

    class Meta:
        unique_together = ('name', 'course_num')
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Grade(models.Model):
    person = models.ForeignKey(
            Person, 
            on_delete=models.CASCADE,
            related_name="grades",
            verbose_name = 'Чья оценка')
    grade = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name = 'Оценка'
    )
    course = models.ForeignKey(
            Course, 
            null=True,
            on_delete=models.CASCADE,
            verbose_name = 'Курс')
    date_add = models.DateField(
            auto_now_add=True, 
            null=True,
            verbose_name = 'Дата добавления')
    date_upd = models.DateField(
            auto_now=True,
            null=True,
            verbose_name = 'Дата изменения')
    date = models.DateField(verbose_name = 'Дата оценки', null=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"    