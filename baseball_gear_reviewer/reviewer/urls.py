from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_gear_list, name='all_gear_list'),
    path('/bat_list', views.bat_list, name='bat_list'),
    path('/bat/<int:id>', views.bat_detail, name='bat_detail'),
    path('/glove_list', views.glove_list, name='glove_list'),
    path('/glove/<int:id>', views.glove_detail, name='glove_detail'),
    path('/ball_list', views.ball_list, name='ball_list'),
    path('/ball/<int:id>', views.ball_detail, name='ball_detail'),
    path('/helmet_list', views.helmet_list, name='helmet_list'),
    path('/helmet/<int:id>', views.helmet_detail, name='helmet_detail'),

    path('review/new', views.review_create, name='review_create'),


    # path('decade/new', views.decade_create, name='decade_create'),
    # path('decade/edit/<int:id>', views.decade_edit, name="decade_edit"),
    # path('decade/delete/<int:id>', views.decade_delete, name='decade_delete'),

    # path('fad_list', views.fad_list, name='fad_list'),
    # path('fad/<int:id>', views.fad_detail, name='fad_detail'),
    # path('fad/new', views.fad_create, name='fad_create'),
    # path('fad/edit/<int:id>', views.fad_edit, name="fad_edit"),
    # path('fad/delete/<int:id>', views.fad_delete, name='fad_delete'),
]