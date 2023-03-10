from django.urls import path
from people_app.views import people_list, person_detail
from . import views


urlpatterns = [
    path('people/', views.people_list, name='people_list'),
    path('people/<int:id>/', views.person_detail, name='person_detail'),
]
