from django.urls import path
from .views import *

urlpatterns = [
    path('page1/', page1, name='page1'),
    path('add_page1/', add_page1, name='add_page1'),
    path('view_intro/',view_intro,name='view_intro'),
]
