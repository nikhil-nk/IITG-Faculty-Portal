# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import professor,department,education,award_fellowships,award_achievement,experience,project,publication_books,publication_conferences,publication_journals,publication_thesis,student_completed,student_ongoing
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,get_object_or_404
from .forms import UserForm
from django.contrib.auth.models import Permission, User
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from django.http import HttpResponse
import urllib

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def index(request):
    all_professors = professor.objects.all()
    return render(request, 'prof/index.html',{'all_professors':all_professors})


def dashboard2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/dashboard.html',{'prof':prof})


def dashboard1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    degree = request.POST['degree']
    field = request.POST['field']
    institute = request.POST['institute']
    year = request.POST['year']
    try:
        p = professor.objects.get(pk=professor_id)
        a = education()
        a.professor = p
        a.first = institute
        a.degree = degree
        a.field = field
        a.year = year

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/dashboard.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/dashboard.html', {'prof': prof})


def my_profile2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/user.html',{'prof':prof})


def my_profile1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    department = request.POST['department']
    first_name = request.POST['first_name']
    middle_name = request.POST['middle_name']
    last_name = request.POST['last_name']
    designation = request.POST['designation']
    email = request.POST['email']
    office = request.POST['office']
    phone = request.POST['phone']
    residence = request.POST['residence']
    university = request.POST['university']
    about_me = request.POST['about_me']
    try:
        p = professor.objects.get(pk=professor_id)
        p.department = department
        p.first_name = first_name
        p.middle_name = middle_name
        p.last_name = last_name
        p.designation = designation
        p.email = email
        p.office = office
        p.phone = phone
        p.residence = residence
        p.about_me = about_me
        p.university = university
    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/user.html', {'prof': prof})
    else:
        p.update()
        return render(request, 'prof/user.html', {'prof': prof})


def education2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/education.html', {'prof': prof})


def education1(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    degree = request.POST['degree']
    field = request.POST['field']
    university = request.POST['university']
    year = request.POST['year']
    try:
        p = professor.objects.get(pk=professor_id)
        a = education()
        a.professor = p
        a.university = university
        a.degree = degree
        a.field = field
        a.year = year
    except (KeyError,professor.DoesNotExist):
        return render(request, 'prof/education.html',{'prof':prof})
    else:
        a.save()
        return render(request, 'prof/education.html',{'prof':prof})


def experience2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/experience.html',{'prof':prof})


def experience1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    designation = request.POST['designation']
    year_end = request.POST['year_end']
    university = request.POST['university']
    year_start = request.POST['year_start']
    try:
        p = professor.objects.get(pk=professor_id)
        a = experience()
        a.professor = p
        a.university = university
        a.designation = designation
        a.year_end = year_end
        a.year_start = year_start

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/education.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/education.html', {'prof': prof})


def projects2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/projects.html',{'prof':prof})


def projects1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    name = request.POST['name']
    FA = request.POST['FA']
    PI = request.POST['PI']
    year_start = request.POST['year_start']
    year_end = request.POST['year_end']
    try:
        p = professor.objects.get(pk=professor_id)
        a = project()
        a.professor = p
        a.name = name
        a.FA = FA
        a.PI = PI
        a.year_start = year_start
        a.year_end = year_end

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/projects.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/projects.html', {'prof': prof})


def courses2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/courses.html',{'prof':prof})


def courses1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    name = request.POST['name']
    code = request.POST['code']
    semester = request.POST['semester']
    year_start = request.POST['year_start']
    year_end = request.POST['year_end']
    try:
        p = professor.objects.get(pk=professor_id)
        a = education()
        a.professor = p
        a.name = name
        a.code = code
        a.semester = semester
        a.year_start = year_start
        a.year_end = year_end

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/courses.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/courses.html', {'prof': prof})


def students2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/student.html',{'prof':prof})


def students1_1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    name = request.POST['name']
    thesis_title = request.POST['thesis_title']
    year_start = request.POST['year_start']
    try:
        p = professor.objects.get(pk=professor_id)
        a = student_ongoing()
        a.professor = p
        a.name = name
        a.thesis_title = thesis_title
        a.year_start = year_start
        a.year_end = 'current'

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/student.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/student.html', {'prof': prof})


def students1_2(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    name = request.POST['name']
    thesis_title = request.POST['thesis_title']
    year_start = request.POST['year_start']
    year_end = request.POST['year_end']
    try:
        p = professor.objects.get(pk=professor_id)
        a = student_completed()
        a.professor = p
        a.name = name
        a.thesis_title = thesis_title
        a.year_start = year_start
        a.year_end = year_end

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/student.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/student.html', {'prof': prof})



def publication2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/publication.html',{'prof':prof})


def publication1_1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    published_at = request.POST['published_at']
    year = request.POST['year']
    description = request.POST['description']
    co_authors = request.POST['co_authors']
    try:
        p = professor.objects.get(pk=professor_id)
        a = publication_journals()
        a.professor = p
        a.published_at = published_at
        a.year = year
        a.description = description
        a.co_authors = co_authors

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/publication.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/publication.html', {'prof': prof})


def publication1_2(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    published_at = request.POST['published_at']
    year = request.POST['year']
    description = request.POST['description']
    co_authors = request.POST['co_authors']
    try:
        p = professor.objects.get(pk=professor_id)
        a = publication_conferences()
        a.professor = p
        a.published_at = published_at
        a.year = year
        a.description = description
        a.co_authors = co_authors

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/publication.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/publication.html', {'prof': prof})


def publication1_3(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    published_at = request.POST['published_at']
    year = request.POST['year']
    description = request.POST['description']
    co_authors = request.POST['co_authors']
    try:
        p = professor.objects.get(pk=professor_id)
        a = publication_books()
        a.professor = p
        a.published_at = published_at
        a.year = year
        a.description = description
        a.co_authors = co_authors

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/publication.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/publication.html', {'prof': prof})


def publication1_4(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    published_at = request.POST['published_at']
    year = request.POST['year']
    description = request.POST['description']
    co_authors = request.POST['co_authors']
    try:
        p = professor.objects.get(pk=professor_id)
        a = publication_thesis()
        a.professor = p
        a.published_at = published_at
        a.year = year
        a.description = description
        a.co_authors = co_authors

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/publication.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/publication.html', {'prof': prof})


def awards2(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/recognitions.html',{'prof':prof})


def awards1_1(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    name = request.POST['name']
    year = request.POST['year']
    awarded_by = request.POST['awarded_by']
    awarded_at = request.POST['awarded_at']
    try:
        p = professor.objects.get(pk=professor_id)
        a = award_achievement()
        a.professor = p
        a.name = name
        a.year = year
        a.awarded_by = awarded_by
        a.awarded_at = awarded_at

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/recognitions.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/recognitions.html', {'prof': prof})


def awards1_2(request,professor_id):
    prof = get_object_or_404(professor, pk=professor_id)
    name = request.POST['name']
    year = request.POST['year']
    awarded_by = request.POST['awarded_by']
    awarded_at = request.POST['awarded_at']
    try:
        p = professor.objects.get(pk=professor_id)
        a = award_fellowships()
        a.professor = p
        a.name = name
        a.year = year
        a.awarded_by = awarded_by
        a.awarded_at = awarded_at

    except (KeyError, professor.DoesNotExist):
        return render(request, 'prof/recognitions.html', {'prof': prof})
    else:
        a.save()
        return render(request, 'prof/recognitions.html', {'prof': prof})


def profile(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/base.html',{'prof':prof})


def profile1(request,professor_id):
    prof = get_object_or_404(professor,pk=professor_id)
    return render(request, 'prof/index-4.html',{'prof':prof})


#
# def index(request):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         albums = Album.objects.filter(user=request.user)
#         song_results = Song.objects.all()
#         query = request.GET.get("q")
#         if query:
#             albums = albums.filter(
#                 Q(album_title__icontains=query) |
#                 Q(artist__icontains=query)
#             ).distinct()
#             song_results = song_results.filter(
#                 Q(song_title__icontains=query)
#             ).distinct()
#             return render(request, 'music/index.html', {
#                 'albums': albums,
#                 'songs': song_results,
#             })
#         else:
#             return render(request, 'music/index.html', {'albums': albums})


def viewprofile(request):
    user=request.user
    prof = user.professor_set.all()

    return render(
        request,
        '',
        {}
    )


@csrf_exempt
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'prof/index.html', context)


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                usr = request.user
                prof = usr.professor

                # prof = professor.objects.filter(user=request.user)
                return render(request, 'prof/user.html', {'prof': prof})
            else:
                return render(request, 'prof/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'prof/login.html', {'error_message': 'Invalid login'})
    return render(request, 'prof/login.html')


@csrf_exempt
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        #
        # test = new professor
        #
        # test.name =
        prof = professor()

        prof.email = username
        prof.first_name = username
        prof.department=department.objects.get(pk=1)
        prof.user = user
        prof.save()

        user.professor=prof


        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                usr = request.user
                prof = usr.professor

                # prof = professor.objects.filter(user=request.user)
                return render(request, 'prof/user.html', {'prof': prof})
    context = {
        "form": form,
    }
    return render(request, 'prof/register.html', context)














def directory(request,department_id):
    dept = get_object_or_404(department,pk=department_id)
    return render(request, 'prof/deptar.html',{'dept':dept})





def notice_board(request):

    url = 'http://intranet.iitg.ernet.in/noticeboard'
    source_code = urllib.urlopen(url)
    plain_text = source_code.read()
    # print(plain_text)
    soup = BeautifulSoup(plain_text, 'html.parser')

    # for x in soup.find('table', {'class': 't1'}).findAll('td', {'valign': 'top'}):
    #     print(x.string)

    y = r""

    for x in soup.find('table', {'class': 't1'}).findAll('a'):
        # print(x.string)
        result = x.string
        link = "http://intranet.iitg.ernet.in" + x.get('href')
        # print(link)

        y+='<a href="' + link + '">' + result + '</a>'
        y+='</br></br>'

# def notice_board(request):
#
#     url = 'http://intranet.iitg.ernet.in/noticeboard'
#     source_code = urllib.urlopen(url)
#     plain_text = source_code.read()
#     # print(plain_text)
#     soup = BeautifulSoup(plain_text, 'html.parser')
#
#         # for x in soup.find('table', {'class': 't1'}).findAll('td', {'valign': 'top'}):
#        #     print(x.string)
#     result = "  {% load staticfiles %}"
#     result += '<link rel="stylesheet" href="{% static "prof/bootstrap.min.css" %}" />'
#
#     result += "<ul class='dropdown-menu'>"
#         for x in soup.find('table', {'class': 't1'}).findAll('a'):
#             y = x.string
#             link = "http://intranet.iitg.ernet.in" + x.get('href')
#             result += '<li><a href="' + link + '">' + y + '</a></li>'
#         result += '</ul>'
#         # print(result)
    return HttpResponse(y)









