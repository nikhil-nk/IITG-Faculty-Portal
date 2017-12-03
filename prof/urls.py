from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views



app_name = 'prof'

urlpatterns = [

    url(r'^$', views.index, name='index'),


    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # url(r'^$', views.index, name="index"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/$', views.dashboard2, name="dashboard"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/update/$', views.dashboard1, name="dashboard1"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/profile/$', views.my_profile2, name="my_profile"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/profile/update/$', views.my_profile1, name="my_profile1"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/education/$', views.education2, name="education"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/education/update/$', views.education1, name="education1"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/experience/$', views.experience2, name="experience"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/experience/update/$', views.experience1, name="experience1"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/projects/$', views.projects2, name="projects"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/projects/update/$', views.projects1, name="projects1"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/courses/$', views.courses2, name="courses"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/courses/update/$', views.courses1, name="courses1"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/students/$', views.students2, name="students"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/students/update/1/$', views.students1_1, name="students1_1"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/students/update/2/$', views.students1_2, name="students1_2"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/publications/$', views.publication2, name="publication"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/publications/update/1/$', views.publication1_1, name="publication1_1"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/publications/update/2/$', views.publication1_2, name="publication1_2"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/publications/update/3/$', views.publication1_3, name="publication1_3"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/publications/update/4/$', views.publication1_4, name="publication1_4"),

    url(r'^dashboard/(?P<professor_id>[0-9]+)/awards/$', views.awards2, name="awards"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/awards/update/1/$', views.awards1_1, name="award1_1"),
    url(r'^dashboard/(?P<professor_id>[0-9]+)/awards/update/2/$', views.awards1_2, name="award1_2"),


    url(r'^directory/(?P<department_id>[0-9]+)/$', views.directory, name="directory"),


    url(r'^(?P<professor_id>[0-9]+)/$', views.profile, name="profile"),
    url(r'^(?P<professor_id>[0-9]+)/1$', views.profile1, name="profile1"),

    # url(r'add/', views.createProfile.as_view(), name="profile_add"),
    url(r'^crawl/$', views.notice_board, name="crawl"),
]
