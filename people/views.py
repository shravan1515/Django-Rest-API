from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
import requests

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

def person_list(request):
    response = requests.get('http://127.0.0.1:8000/api/people/')
    people = response.json()
    return render(request, "people/list.html", {'people': people})
def person_create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'age': request.POST['age'],
            'city': request.POST['city'],
        }
        requests.post('http://127.0.0.1:8000/api/people/', data=data)
        return redirect('/people/')
    return render(request, 'people/form.html', {'title': 'Create Person'})

def person_update(request, id):
    url = f'http://127.0.0.1:8000/api/people/{id}/'
    if request.method == 'POST':
        data = {
            'name': request.POST['name'],
            'age': request.POST['age'],
            'city': request.POST['city'],
        }
        requests.put(url, data=data)
        return redirect('/people/')
    person = requests.get(url).json()
    return render(request, 'people/form.html', {'title': 'Update Person', 'person': person})

def person_delete(request, id):
    url = f'http://127.0.0.1:8000/api/people/{id}/'
    requests.delete(url)
    return redirect('/people/')
