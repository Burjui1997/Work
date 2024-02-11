from django.urls import path
from cards import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:card_id>/', views.get_card_by_id, name='card'),
]
