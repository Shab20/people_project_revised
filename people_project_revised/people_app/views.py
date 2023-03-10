from django.shortcuts import render
from django.views.generic import DetailView
from .models import Person
from django.http import HttpResponse


PEOPLE = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def people_list(request):
    people = sorted(PEOPLE, key=lambda person: person['age'])
    return render(request, 'people_list.html', {'people': people})

def person_detail(request, id):
    person = next((person for person in PEOPLE if person['id'] == id), None)
    return render(request, 'person_detail.html', {'person': person})



