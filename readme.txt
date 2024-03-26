git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/netphoenix/django_tst2.git
git push -u origin main

pip install django
pip install pillow
pip install django-debug-toolbar
pip install djangorestframework

django-admin.exe startproject setting .
python manage.py startapp scool

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python.exe manage.py runserver  

sudo apt update
sudo apt install python3-dev
sudo apt install python3-venv
sudo apt install python3-pip
sudo apt install -y nginx
sudo apt install -y libpq-dev
sudo apt install -y supervisor

python3 -m venv .venv
source .venv/bin/activate

pip install gunicorn

nano flask1.py
nano wsgi.py
gunicorn -b 0.0.0.0:7773 wsgi:app

ls /etc/nginx/
ls /etc/nginx/sites-enabled/
sudo nano /etc/nginx/sites-enabled/default 
sudo service nginx restart
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header Cookie $http_cookie;
                proxy_set_header Host $http_host;
ls /etc/supervisor/conf.d/
sudo nano /etc/supervisor/conf.d/flask1.conf
    [program:flask1]
    command = /home/nightsolarghost/flask_tst/venv/bin/gunicorn -b 127.0.0.1:7774 -w 4 --timeout 904 wsgi:app
    autostart = true
    autorestart = true
    directory = home/nightsolarghost/flask_tst/
    stderr_logfile = /var/log/flask_tst.err.log
    stdout_logfile = /var/log/flask_tst.out.log
        command = /home/nightsolarghost/django_tst2/.venv/bin/gunicorn setting.wsgi -b 127.0.0.1:8000 -w 8 --timeout 90
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart flask1
sudo supervisorctl stop flask1

settings.py
-----------
INSTALLED_APPS = [
    'scool.apps.ScoolConfig',

TEMPLATES = [
        'DIRS': ['templates'],

LANGUAGE_CODE = 'ru-RU'

# STATIC_ROOT = Path(BASE_DIR, 'static') # ��� ������ �� ������ 
STATICFILES_DIRS = [Path(BASE_DIR, 'static')]

ALLOWED_HOSTS = ['*']


apps.py
-------
    verbose_name = "�������� �"

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
            verbose_name = '���'
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
            verbose_name = '�������')
    age = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(12), MaxValueValidator(99)],
        verbose_name = '�������'
    )
    course = models.ManyToManyField(
            'Course', 
            blank=True,
            verbose_name = '���������� �����')  
    

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} {self.age}'

    class Meta:
        indexes= [models.Index(fields=['first_name'])]
        # ordering = ['first_name']
        verbose_name = "������"
        verbose_name_plural = "�������"
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
        verbose_name = '������������')
    course_num = models.SmallIntegerField(
            default=0,
            verbose_name = '����� �����')
  
    start_date = models.DateField(verbose_name = '������ �����', null=True)
    end_date = models.DateField(verbose_name = '��������� �����', null=True)
    
    def __str__(self) -> str:
        return f'{self.get_name_display()}-{self.course_num}'

    class Meta:
        unique_together = ('name', 'course_num')
        verbose_name = "����"
        verbose_name_plural = "�����"


class Grade(models.Model):
    person = models.ForeignKey(
            Person, 
            on_delete=models.CASCADE,
            related_name="grades",
            verbose_name = '��� ������')
    grade = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name = '������'
    )
    course = models.ForeignKey(
            Course, 
            null=True,
            on_delete=models.CASCADE,
            verbose_name = '����')
    date_add = models.DateField(
            auto_now_add=True, 
            null=True,
            verbose_name = '���� ����������')
    date_upd = models.DateField(
            auto_now=True,
            null=True,
            verbose_name = '���� ���������')
    date = models.DateField(verbose_name = '���� ������', null=True)

    class Meta:
        verbose_name = "������"
        verbose_name_plural = "������"    



admin.py
--------
rom .models import Person, Course, Grade
# Register your models here.

# admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # ���������� ������ ��� ����
    list_display=('last_name', 'first_name', 'average_grade1', 'average_grade2')    
    
    # �������� ����� �� ������ 
    search_fields = ('last_name__startswith',)
    # search_fields = ('last_name',)

    # �������� ������
    list_filter = ('first_name',)

    # ���������� �������� ����
    def average_grade1(self, obj):
        from django.db.models import Avg
        res = Grade.objects.filter(person=obj).aggregate(Avg('grade', default=0))
        return res['grade__avg']
    
    def average_grade2(self, obj):        
        gs = [g.grade for g in obj.grades.all()]
        return round(sum(gs)/len(gs),2) if gs else '---'

    average_grade1.short_description = "������� ������"

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
|  last_name   |  varchar(25)     |  YES |     |  NULL   |      ���       |
|  first_name  |  varchar(25)     |  YES |     |  NULL   |    �������     |
|     age      |  smallint(5)     |  YES |     |    0    |    �������     |
+--------------+------------------+------+-----+---------+----------------+

Course:
+--------------+------------------+------+-----+---------+----------------+
|   Column     |       Type       | Null | Key | Default |    Comment     |
+--------------+------------------+------+-----+---------+----------------+
|   id         |   int(11)        |  NO  | PRI |  NULL   |   Primary Key  |
|     name     |  varchar(25)     |  YES |     |  NULL   |  ������������  |
| course_num   |  smallint(5)     |  YES |     |    0    |  ����� �����   |
| start_date   |  date            |  YES |     |  NULL   |  ������ �����  |
|  end_date    |  date            |  YES |     |  NULL   | ��������� �����|
+--------------+------------------+------+-----+---------+----------------+

Grade:
+--------------+------------------+------+-----+---------+----------------+
|   Column     |       Type       | Null | Key | Default |    Comment     |
+--------------+------------------+------+-----+---------+----------------+
|   id         |   int(11)        |  NO  | PRI |  NULL   |   Primary Key  |
|   person_id  |   int(11)        |  YES | MUL |  NULL   |  ��� ������    |
|    grade     |  smallint(5)     |  YES |     |    0    |     ������     |
|  course_id   |   int(11)        |  YES | MUL |  NULL   |     ����       |
|  date_add    |      date        |  YES |     |  NULL   | ���� ����������|
|  date_upd    |      date        |  YES |     |  NULL   | ���� ��������� |
|     date     |      date        |  YES |     |  NULL   |  ���� ������   |
+--------------+------------------+------+-----+---------+----------------+
