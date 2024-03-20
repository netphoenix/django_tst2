git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/netphoenix/django_tst2.git
git push -u origin main

pip install django

django-admin.exe startproject setting .
python manage.py startapp scool

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python.exe manage.py runserver  



settings.py
-----------
INSTALLED_APPS = [
    'scool.apps.ScoolConfig',

TEMPLATES = [
        'DIRS': ['templates'],

LANGUAGE_CODE = 'ru-RU'

# STATIC_ROOT = Path(BASE_DIR, 'static') # для деплоя на сервер 
STATICFILES_DIRS = [Path(BASE_DIR, 'static')]

ALLOWED_HOSTS = ['*']


apps.py
-------
    verbose_name = "Академия У"

urls.py
-------
from scool import views
    path('', views.index, name='index'),



views.py
--------
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hello')
    return render(request, '1.html', {'data':'Hello'})  


models.py
---------
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
        verbose_name = 'Возраст'
    )
    course = models.ManyToManyField(
            'Course', 
            blank=True,
            verbose_name = 'Посещаемые курсы')  
    

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.age}'

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
    
    def __str__(self) -> str:
        return f'{self.get_name_display()}-{self.course_num}'

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



admin.py
--------
rom .models import Person, Course, Grade
# Register your models here.

# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # показывать только эти поля
    list_display=('last_name', 'first_name', 'average_grade1', 'average_grade2')    
    
    # добавить поиск по полямм 
    search_fields = ('last_name__startswith',)
    # search_fields = ('last_name',)

    # добавить фильтр
    list_filter = ('first_name',)

    # вычисление среднего бала
    def average_grade1(self, obj):
        from django.db.models import Avg
        res = Grade.objects.filter(person=obj).aggregate(Avg('grade', default=0))
        return res['grade__avg']
    
    def average_grade2(self, obj):        
        gs = [g.grade for g in obj.grades.all()]
        return round(sum(gs)/len(gs),2) if gs else '---'

    average_grade1.short_description = "Средняя оценка"

@admin.register(Course)
class PersonCourse(admin.ModelAdmin):
    list_display=('name', 'course_num', 'start_date', 'end_date')    
    search_fields = ('name',)
    list_filter = ('name',)

    
    
@admin.register(Grade)
class PersonGrade(admin.ModelAdmin):
    list_display=('person', 'grade', 'date', 'course')            





Person:
+--------------+------------------+------+-----+---------+----------------+
|   Column     |       Type       | Null | Key | Default |    Comment     |
+--------------+------------------+------+-----+---------+----------------+
|   id         |   int(11)        |  NO  | PRI |  NULL   |   Primary Key  |
|  last_name   |  varchar(25)     |  YES |     |  NULL   |      Имя       |
|  first_name  |  varchar(25)     |  YES |     |  NULL   |    Фамилия     |
|     age      |  smallint(5)     |  YES |     |    0    |    Возраст     |
+--------------+------------------+------+-----+---------+----------------+

Course:
+--------------+------------------+------+-----+---------+----------------+
|   Column     |       Type       | Null | Key | Default |    Comment     |
+--------------+------------------+------+-----+---------+----------------+
|   id         |   int(11)        |  NO  | PRI |  NULL   |   Primary Key  |
|     name     |  varchar(25)     |  YES |     |  NULL   |  Наименование  |
| course_num   |  smallint(5)     |  YES |     |    0    |  Номер курса   |
| start_date   |  date            |  YES |     |  NULL   |  Начало курса  |
|  end_date    |  date            |  YES |     |  NULL   | Окончание курса|
+--------------+------------------+------+-----+---------+----------------+

Grade:
+--------------+------------------+------+-----+---------+----------------+
|   Column     |       Type       | Null | Key | Default |    Comment     |
+--------------+------------------+------+-----+---------+----------------+
|   id         |   int(11)        |  NO  | PRI |  NULL   |   Primary Key  |
|   person_id  |   int(11)        |  YES | MUL |  NULL   |  Чья оценка    |
|    grade     |  smallint(5)     |  YES |     |    0    |     Оценка     |
|  course_id   |   int(11)        |  YES | MUL |  NULL   |     Курс       |
|  date_add    |      date        |  YES |     |  NULL   | Дата добавления|
|  date_upd    |      date        |  YES |     |  NULL   | Дата изменения |
|     date     |      date        |  YES |     |  NULL   |  Дата оценки   |
+--------------+------------------+------+-----+---------+----------------+
