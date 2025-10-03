"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from notes_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Notes Flow URLs
    path('notes/', views.select_language, name='select_language'),
    path('notes/<int:language_id>/branch/', views.select_branch, name='select_branch'),
    path('notes/<int:language_id>/<int:branch_id>/semester/', views.select_semester, name='select_semester'),
    path('notes/<int:language_id>/<int:branch_id>/<int:semester_id>/subject/', views.select_subject, name='select_subject'),
    path('notes/<int:language_id>/<int:branch_id>/<int:semester_id>/<int:subject_id>/unit/', views.select_unit, name='select_unit'),
    path('notes/<int:language_id>/<int:branch_id>/<int:semester_id>/<int:subject_id>/<int:unit_id>/view/', views.view_note, name='view_note'),
    
    # Previous Papers URLs
    path('papers/', views.papers_list, name='papers_list'),
    # path('papers/<int:paper_id>/', views.view_paper, name='view_paper'),

    # path('papers/', views.papers_list, name='papers_list'),
    # path('papers/download/<int:paper_id>/', views.download_paper, name='download_paper'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
