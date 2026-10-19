# -*- coding: utf-8 -*-
from django.urls import path

from .views import home, ajuda

urlpatterns = [
  path('', home),
  path('ajuda', ajuda),
]
