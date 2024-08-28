from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dataadmin/', views.dataadmin, name='dataadmin'),
    path('startinventur/<int:loc_id>', views.startinventur, name='startinventur'),# was ist das?
    path('inventur/<int:inv_id>', views.inventur, name='inventur'),
    path('boxtyp/<int:box_id>', views.boxtyp_data, name='boxtyp'),
    path('location/<int:loc_id>', views.location_data, name='location'),
    path('item/<int:item_id>/', views.item_data, name='item'),
    path('updateinvitem', views.updateinvitem, name='updateinvitem'),# und das?
]
