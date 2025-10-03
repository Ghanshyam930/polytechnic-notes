# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import login, logout, authenticate
# from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# from .models import (Language, Branch, Semester, Subject, Unit, Note, 
#                     PreviousPaper, Profile)
# from django.core.paginator import Paginator

# def home(request):
#     return render(request, 'notes_app/home.html')

# def about(request):
#     return render(request, 'notes_app/about.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'notes_app/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'notes_app/login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('home')

# @login_required
# def dashboard(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, 'Your profile has been updated!')
#             return redirect('dashboard')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
    
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'notes_app/dashboard.html', context)

# # Notes Flow Views
# # @login_required
# def select_language(request):
#     languages = Language.objects.all()
#     return render(request, 'notes_app/notes/language.html', {'languages': languages})

# # @login_required
# def select_branch(request, language_id):
#     branches = Branch.objects.all()
#     return render(request, 'notes_app/notes/branch.html', {
#         'branches': branches,
#         'language_id': language_id
#     })

# # @login_required
# def select_semester(request, language_id, branch_id):
#     branch = get_object_or_404(Branch, pk=branch_id)
#     semesters = branch.semester_set.all()
#     return render(request, 'notes_app/notes/semester.html', {
#         'semesters': semesters,
#         'language_id': language_id,
#         'branch_id': branch_id
#     })

# # @login_required
# def select_subject(request, language_id, branch_id, semester_id):
#     semester = get_object_or_404(Semester, pk=semester_id)
#     subjects = Subject.objects.filter(semester=semester, branch_id=branch_id)
#     return render(request, 'notes_app/notes/subject.html', {
#         'subjects': subjects,
#         'language_id': language_id,
#         'branch_id': branch_id,
#         'semester_id': semester_id
#     })

# # @login_required
# def select_unit(request, language_id, branch_id, semester_id, subject_id):
#     subject = get_object_or_404(Subject, pk=subject_id)
#     units = Unit.objects.filter(subject=subject)
#     return render(request, 'notes_app/notes/unit.html', {
#         'units': units,
#         'language_id': language_id,
#         'branch_id': branch_id,
#         'semester_id': semester_id,
#         'subject_id': subject_id
#     })

# @login_required

# def view_note(request, language_id, branch_id, semester_id, subject_id, unit_id):
#     unit = get_object_or_404(Unit, pk=unit_id)
#     notes = Note.objects.filter(unit=unit, language_id=language_id)
#     return render(request, 'notes_app/notes/view_note.html', {
#         'notes': notes,
#         'language_id': language_id,
#         'branch_id': branch_id,
#         'semester_id': semester_id,
#         'subject_id': subject_id,
#         'unit_id': unit_id
#     })


# # Previous Papers Views
# # @login_required
# def papers_list(request):
#     branches = Branch.objects.all().prefetch_related('semesters')
#     papers = PreviousPaper.objects.select_related('subject', 'subject__branch', 'subject__semester').all()
#     return render(request, 'papers.html', {
#         'branches': branches,
#         'papers': papers
#     })

# @login_required
# def view_paper(request, paper_id):
#     paper = get_object_or_404(PreviousPaper, pk=paper_id)
#     return render(request, 'notes_app/papers/view_paper.html', {'paper': paper})




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import (Language, Branch, Semester, Subject, Unit, Note, 
                    PreviousPaper, Profile)


def home(request):
    return render(request, 'notes_app/home.html')


def about(request):
    return render(request, 'notes_app/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'notes_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'notes_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'notes_app/dashboard.html', context)


# ----------------- NOTES FLOW -----------------

def select_language(request):
    languages = Language.objects.all()
    return render(request, 'notes_app/notes/language.html', {'languages': languages})


def select_branch(request, language_id):
    branches = Branch.objects.filter(language_id=language_id)
    return render(request, 'notes_app/notes/branch.html', {
        'branches': branches,
        'language_id': language_id
    })


def select_semester(request, language_id, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id, language_id=language_id)
    semesters = Semester.objects.filter(branches=branch, language_id=language_id)
    return render(request, 'notes_app/notes/semester.html', {
        'semesters': semesters,
        'language_id': language_id,
        'branch_id': branch_id
    })


def select_subject(request, language_id, branch_id, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id, language_id=language_id)
    subjects = Subject.objects.filter(
        semester=semester, branch_id=branch_id, language_id=language_id
    )
    return render(request, 'notes_app/notes/subject.html', {
        'subjects': subjects,
        'language_id': language_id,
        'branch_id': branch_id,
        'semester_id': semester_id
    })


def select_unit(request, language_id, branch_id, semester_id, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id, language_id=language_id)
    units = Unit.objects.filter(subject=subject, language_id=language_id)
    return render(request, 'notes_app/notes/unit.html', {
        'units': units,
        'language_id': language_id,
        'branch_id': branch_id,
        'semester_id': semester_id,
        'subject_id': subject_id
    })


@login_required
def view_note(request, language_id, branch_id, semester_id, subject_id, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id, language_id=language_id)
    notes = Note.objects.filter(unit=unit, language_id=language_id)
    return render(request, 'notes_app/notes/view_note.html', {
        'notes': notes,
        'language_id': language_id,
        'branch_id': branch_id,
        'semester_id': semester_id,
        'subject_id': subject_id,
        'unit_id': unit_id
    })


# ----------------- PREVIOUS PAPERS -----------------

# def papers_list(request):
#     branches = Branch.objects.all().prefetch_related('semester_set')
#     papers = PreviousPaper.objects.select_related(
#         'subject', 'subject__branch', 'subject__semester'
#     ).all()
#     return render(request, 'papers.html', {
#         'branches': branches,
#         'papers': papers
#     })
def papers_list(request):
    papers = PreviousPaper.objects.all().order_by('-year')[:15]  # Last 3 years (assuming 5 per year)
    return render(request, 'notes_app/papers/papers.html', {'papers': papers})

# @login_required
# def view_paper(request, paper_id):
#     paper = get_object_or_404(PreviousPaper, pk=paper_id)
#     return render(request, 'notes_app/papers/view_paper.html', {'paper': paper})

