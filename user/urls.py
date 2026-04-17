from django.urls import path

from . import views
urlpatterns=[
    path('index1/',views.index),
    path('',views.index1),
    path('home/',views.index1),
    path('about/',views.about),
    path('alumny/',views.alumny),
    path('contact/',views.contact),
    path('courses/',views.courses),
    path('faculty/',views.faculty),
    path('feedback/',views.feedback),
    path('gallery/',views.gallery),
    path('infra/',views.infra),
    path('recruiters/',views.recruiters),
    path('primsg/',views.primsg),

]