from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('item', views.postData),
    path('item/<str:object_id>', views.getItem),
    path('list', views.searchData),
]
