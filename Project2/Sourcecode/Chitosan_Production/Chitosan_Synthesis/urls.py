
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('chitosan_login/', views.chitosan_login),
    path('chitosan_register/', views.chitosan_register),
    path('chitosan_logout/', views.chitosan_logout),
    path('chitosan_home/', views.chitosan_home_page),


    ## VIEW DATA
    path('deacetyl_chitosan_report_view/',            views.deacetyl_chitosan_viewdata),
    path('deacetyl_chitosan_detailedview/<int:id>/',  views.deacetyl_chitosan_detailedview),

    ### Method Adoption Page
    path('chitosan_method_page/',                    views.chitosan_method_page),
    path('chitosan_method_selection_page/<int:id>/', views.chitosan_method_selection_page),



    #### Process Page
    path('chitosan_start_process_page/',     views.chitosan_start_process_page),
    path('chitosan_start_analyse/<int:id>/', views.chitosan_start_analyse),

    # # # ## Report Page
    path('chitosan_report_page/',          views.chitosan_report_page),
    path('chitosan_report_view/<int:id>/', views.chitosan_report_view),

    # ### Encryption Page
    path('chitosan_report_encryption/<int:id>/',      views.chitosan_report_encryption),
    path('send_encrypt_key/<int:id>/',                 views.send_encrypt_key),
]
