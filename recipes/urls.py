from django.urls import path
from recipes.views import home
from recipes import views
#  from . import views


urlpatterns = [
    path('', views.home), #Home
    path('recipes/<int:id>/', views.recipe), #Home
] 