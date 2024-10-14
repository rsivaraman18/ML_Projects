
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('mineral_login/',    views.mineral_login),
    path('mineral_register/', views.mineral_register),
    path('mineral_logout/',   views.mineral_logout),
    path('mineral_home/',     views.mineral_home_page),


    ## VIEW DATA
    path('mineral_viewdata/',      views.mineral_viewdata),
    path('mineral_data/<int:id>/', views.mineral_view_reports_data),

    # Upload Dataset Page
    path('mineral_dataset_upload/', views.mineral_dataset_upload),

    # # ## Process Page
    path('mineral_start_process_page/',     views.mineral_start_process),
    path('mineral_start_analyse/<int:id>/', views.mineral_start_analyse),

    # # ## Efficiency Calculation
    path('mineral_calculation_page/',         views.mineral_calculation_page),
    path('mineral_start_calculate/<int:id>/', views.mineral_start_calculate),

    # # # ## Report Page
    path('mineral_report_page/',          views.mineral_report_page),
    path('mineral_report_view/<int:id>/', views.mineral_report_view),
]
