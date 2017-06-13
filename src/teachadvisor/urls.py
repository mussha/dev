"""teachadvisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView, PromotionView, ContactView, TermsAndConditionView, UserAgreementView, PrivacyPolicyView, Test

from teacher.views import TeacherCreate, TeacherUpdate, TeacherList, TeacherDetail, FavTeacherList
from opening.views import OpeningCreate, OpeningList, OpeningUpdate, OpeningDetail, FavOpeningList, POpeningList, POpeningListInactive
from student.views import StudentCreate, StudentUpdate, StudentList, StudentDetail


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', HomeView.as_view(), name='Home'),
    url(r'^contact/$', ContactView.as_view(), name='Contact'),
    url(r'^promotions/$', PromotionView.as_view(), name='Promotions'),

    url(r'^termsandconditions/$', TermsAndConditionView.as_view(), name='TermsAndCondition'),
    url(r'^useragreement/$', UserAgreementView.as_view(), name='UserAgreement'),
    url(r'^privacypolicy/$', PrivacyPolicyView.as_view(), name='PrivacyPolicy'),

    # url(r'^test/$', Test, name='Test'),

    #worker details
    url(r'^teacher/add/$', TeacherCreate.as_view(), name='TeacherCreate'),
    url(r'^teacher/$', TeacherList.as_view(), name='TeacherList'),
    url(r'^teacher/(?P<pk>[0-9]+)/edit$', TeacherUpdate.as_view(), name='TeacherUpdate'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', TeacherDetail.as_view(), name='TeacherDetail'),

    #company details
    url(r'^student/add/$', StudentCreate.as_view(), name='StudentCreate'),
    url(r'^student/$', StudentList.as_view(), name='StudentList'), #to block when live
    url(r'^student/(?P<pk>[0-9]+)/edit$', StudentUpdate.as_view(), name='StudentUpdate'),
    url(r'^student/(?P<pk>[0-9]+)/$', StudentDetail.as_view(), name='StudentDetail'),

    #openings
    url(r'^opening/add/$', OpeningCreate.as_view(), name='OpeningCreate'),
    url(r'^opening/$', OpeningList.as_view(), name='OpeningList'),
    url(r'^opening/(?P<pk>[0-9]+)/edit$', OpeningUpdate.as_view(), name='OpeningUpdate'),
    url(r'^opening/(?P<pk>[0-9]+)/$', OpeningDetail.as_view(), name='OpeningDetail'),



]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
