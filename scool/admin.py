from django.contrib import admin

# Register your models here.

from .models import Person, Course, Grade

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