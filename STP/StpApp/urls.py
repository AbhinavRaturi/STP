from django.contrib import admin
from django.urls import path
from . import views
from .views import GeneratePDF
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('officer', views.handelofficer, name='officer'),
    path('officerlogin', views.handleofficerLogin, name='handleofficerLogin'),
    path('officerlogout', views.handleofficerLogout, name='handleofficerLogout'),
    path('deleterecent', views.deleterecent, name='deleterecent'),
    path('acceptrecent', views.acceptrecent, name='acceptrecent'),
    path('sendmails', views.sendmails, name='sendmails'),
    url(r'^admin/', admin.site.urls),
    path('mentor', views.handleteacher, name='handleteacher'),
    path('teacherlogin', views.handleteacherLogin, name='handleteacherLogin'),
    path('teacherlogout', views.handleteacherLogout, name='handleteacherLogout'),
    path('treviewfile1', views.treview1test, name='treview1test'),
    path('treviewfile2', views.treview2test, name='treview2test'),
    path('treviewfile3', views.treview3test, name='treview3test'),
    path('treview1mark', views.treview1marks, name='treview1marks'),
    path('treview2mark', views.treview2marks, name='treview2marks'),
    path('treview3mark', views.treview3marks, name='treview3marks'),


    path('studentAcc', views.handlestudent, name='handlestudent'),
    path('studentlogin', views.handlestudentLogin, name='handlestudentLogin'),
    path('studentlogout', views.handlestudentLogout, name='handlestudentLogout'),

    path('sreviewfile1', views.sreview1test, name='sreview1test'),
    path('sreviewfile2', views.sreview2test, name='sreview2test'),
    path('sreviewfile3', views.sreview3test, name='sreview3test'),
    url(r'^pdf/$', GeneratePDF.as_view()),


]
