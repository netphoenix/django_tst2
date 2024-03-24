"""
URL configuration for setting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from scool.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index',),

    path('persons/', persons, name='persons', kwargs={'id':0}),
    path('persons/<int:id>', persons, name='person',),
    path('persons/add/', PersonAdd.as_view(), name='addperson',),
    path('persons/edit/<int:id>', index, name='editperson',),

    path('courses/', cache_page(50*15)(Courses.as_view()), name='courses',),
    path('courses/<int:id>', Show_course.as_view(), name='course',),
    path('courses/add/', course_add_view, name='addcourse',),
    path('courses/edit/<int:id>', course_edit_view, name='editcourse',),

    path('reg/', RegisterUser.as_view(), name='reg',),
    path('login/', LoginUser.as_view(), name='login',),
    path('logout/', logout_user, name='logout',),
    
    
    # path('verify_code/<str:code>', course_edit_view, name='editcourse',),

]

if settings.DEBUG:
    # django debug toolbar
    # python -m pip install django-debug-toolbar
    import debug_toolbar
    urlpatterns = [path("__debug__/", include("debug_toolbar.urls")),] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
