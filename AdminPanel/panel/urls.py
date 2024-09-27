from django.urls import path
from .views import dashboard ,partner_list, add_partner, partner_details, edit_partner

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('partners/', partner_list, name='partner_list'),
    path('partners/add/', add_partner, name='add_partner'),
    path('partners/<int:partner_id>/', partner_details, name='partner_details'),
    path('partners/edit/<int:partner_id>/', edit_partner, name='edit_partner'),
]


