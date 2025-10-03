# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     branch = models.CharField(max_length=100, blank=True)
#     semester = models.IntegerField(default=1)
    
#     def __str__(self):
#         return f'{self.user.username} Profile'

# class Language(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class Branch(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=10)
    
#     def __str__(self):
#         return self.name

# class Semester(models.Model):
#     number = models.IntegerField()
#     branches = models.ManyToManyField(Branch)
    
#     def __str__(self):
#         return f'Semester {self.number}'

# class Subject(models.Model):
#     name = models.CharField(max_length=200)
#     code = models.CharField(max_length=20)
#     semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
#     branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name

# class Unit(models.Model):
#     number = models.IntegerField()
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'Unit {self.number} - {self.subject.name}'

# class Note(models.Model):
#     title = models.CharField(max_length=200)
#     unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     language = models.ForeignKey(Language, on_delete=models.CASCADE)
#     content = models.TextField(blank=True, null=True)  # yha document likhne ka option
#     uploaded_at = models.DateTimeField(default=timezone.now)
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# class PreviousPaper(models.Model):
#     year = models.IntegerField()
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='papers/')
#     uploaded_at = models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         return f'{self.subject.name} - {self.year}'

# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100, blank=True)
    semester = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.user.username} Profile'


class Language(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    number = models.IntegerField()
    branches = models.ManyToManyField(Branch)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Semester {self.number}'


class Subject(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    number = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Unit {self.number} - {self.subject.name}'


class Note(models.Model):
    title = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)  # document likhne ka option

    def __str__(self):
        return self.title



class PreviousPaper(models.Model):
    year = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(upload_to='papers/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    # language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.subject.name} - {self.year}'
