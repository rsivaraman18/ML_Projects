
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('deacetyl_login/', views.deacetyl_login),
    path('deacetyl_register/', views.deacetyl_register),
    path('deacetyl_logout/', views.deacetyl_logout),
    path('deacetyl_home/', views.deacetyl_home_page),



## VIEW DATA
    path('deacetylation_mineral_report_page/',              views.deacetylation_mineral_report_page),
    path('deacetylation_mineral_detailed_report/<int:id>/', views.deacetylation_mineral_detailed_report),

    # Upload Dataset Page
    path('deacetylation_dataset_upload/', views.deacetylation_dataset_upload),


    # ## Process Page
    path('deacetyl_process_page/',              views.deacetyl_process_page),
    path('deacetyl_start_process/<int:id>/',    views.deacetyl_start_process),


    # # ## Efficiency Calculation
    path('deacetyl_calculation_page/',         views.deacetyl_calculation_page),
    path('deacetyl_start_calculate/<int:id>/', views.deacetyl_start_calculate),


    # # ## Report Page
    path('deacetyl_report_page/',                 views.deacetyl_report_page),
    path('deacetyl_report_detail_view/<int:id>/', views.deacetyl_report_detail_view),
]
