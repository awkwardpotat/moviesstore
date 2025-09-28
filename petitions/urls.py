from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('<int:id>/', views.show, name='petitions.show'),
    path('new_petition_show/', views.new_petition_show, name='petitions.new_petition_show'),
    path('create_petition/', views.create_petition, name='petitions.create_petition'),
    path('vote/<int:id>', views.vote, name='petitions.vote')
]