from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index,  name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
]

# 컨트롤러 역할
# path (받은 맵핑 , 보낼 페이지 이름 , 페이지 별칭)