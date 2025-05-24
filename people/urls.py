from django.urls import (path, include)
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, person_list, person_create, person_update, person_delete

router = DefaultRouter()
router.register(r'api/people', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('people/', person_list),
    path('people/create/', person_create),
    path('people/update/<int:id>', person_update),
    path('people/delete/<int:id>', person_delete),

]
