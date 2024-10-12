from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('deprotein_login/',    views.deprotein_login),
    path('deprotein_register/', views.deprotein_register),
    path('deprotein_logout/',   views.deprotein_logout),
    path('deprotein_home/',     views.deprotein_home_page),

    ## VIEW DATA
    path('deproteinization_viewdata/',               views.deproteinization_viewdata),
    path('deproteinization_detailed_data/<int:id>/', views.deproteinization_detailed_data),
    #
    # Upload Dataset Page
    path('deproteimization_dataset_upload/', views.deproteinization_dataset_upload),

    # ## Process Page
    path('start_process_page/',           views.deproteinization_start_process),
    path('start_analyse/<int:id>/',       views.deproteinization_start_analyse),

    # # ## Report Page
    path('deproteinization_report_page/',          views.deproteinization_report_page),
    path('deproteinization_report_view/<int:id>/', views.deproteinization_report_view),


]
