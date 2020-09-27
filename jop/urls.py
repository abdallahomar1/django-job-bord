from django.urls import path, include
from . import views
app_name='jop'
urlpatterns = [
    path('', views.jop_list),
    path('add', views.add_job, name='add_job'),
    path('<int:id>', views.jop_deteil, name='job_detail'),
]