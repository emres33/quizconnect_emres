from django.urls import path
from . import views
from .models import User
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("home/<str:user_id>", views.home, name="home"),
    path("profile<str:user_id>", views.profile, name="profile"),
    path("add", views.addQuestion, name="addQuestion"),
    path("details/<int:pk>", views.questionDetail, name="details"),
    path("lessons", views.lessons, name="lessons"),
    path("lessons/<str:name>", views.lessonDetails, name="lessonDetails"),
    path('index/', views.index, name='index'),
    path('addQuestion/', views.addQuestion, name='addQuestion'),
    path('save_question/', views.save_question, name='save_question'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)