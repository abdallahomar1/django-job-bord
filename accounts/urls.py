from django.urls import path, include
from . import views
app_name='jop'
urlpatterns = [
    path('signup', views.signup, name= 'signup'),
    path('profile', views.profile, name= 'profile'),
    path('profile/edit', views.profileedite, name= 'profile_edit'),

]