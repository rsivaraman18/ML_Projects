
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('manager_home/',  views.manager_home_page),
    path('manager_login/', views.manager_login_page),
    path('manager_logout/', views.manager_login_out),

    # ### LOGIN ACCESS MODULE 1
    path('manager_dep_access_page/',             views.manager_dep_access_page),
    path('manager_dep_access_approve/<int:id>/', views.manager_dep_access_approve),
    path('manager_dep_access_deny/<int:id>/',    views.manager_dep_access_deny),


    ### LOGIN ACCESS MODULE 2
    path('manager_mineral_access_page/',             views.manager_mineral_access_page),
    path('manager_mineral_access_approve/<int:id>/', views.manager_mineral_access_approve),
    path('manager_mineral_access_deny/<int:id>/',    views.manager_mineral_access_deny),


    # ### LOGIN ACCESS MODULE 3
    path('manager_deacetyl_access_page/',             views.manager_deacetyl_access_page),
    path('manager_deacetyl_access_approve/<int:id>/', views.manager_deacetyl_access_approve),
    path('manager_deacetyl_access_deny/<int:id>/',    views.manager_deacetyl_access_deny),


    # # ### LOGIN ACCESS MODULE 4
    path('manager_chitosan_access_page/',             views.manager_chitosan_access_page),
    path('manager_chitosan_access_approve/<int:id>/', views.manager_chitosan_access_approve),
    path('manager_chitosan_access_deny/<int:id>/',    views.manager_chitosan_access_deny),

    # ### UPLOAD PAGE FOR NEW REQUIREMENT
    path('manager_upload_requirement_page/', views.manager_upload_requirement_page),
    path('manager_upload_new_requirement/',  views.manager_upload_new_requirement),



    ################# REPORT APPROVAL ZONE STARTS HERE   ############################


    #### TEAM 1 ----> Deproteinization TEAM REPORTS,VIEW,APPROVE,DENY  #################
    
    #### TEAM 1 ----> REPORT PAGE & Detailed Report View
    path('deproteinization_report_page/',          views.deproteinization_report_page),
    path('deproteinization_report_view/<int:id>/', views.deproteinization_report_view),

    ### TEAM 1 ----> APPROVE & REJECT
    path('deproteinization_report_mng_approve/<int:id>/', views.deproteinization_report_mng_approve),
    path('deproteinization_report_mng_reject/<int:id>/',  views.deproteinization_report_mng_reject),

    ########################################################################################


    ### TEAM 2 ----> Mineral Separation --> TEAM REPORTS,VIEW,APPROVE,DENY  

    ### TEAM 2 ----> REPORT PAGE & Detailed Report View
    path('mineral_report_page/',          views.mineral_report_page),
    path('mineral_report_view/<int:id>/', views.mineral_report_view),
    
    ## TEAM 2 ----> APPROVE & REJECT
    path('mineral_mng_approve/<int:id>/', views.mineral_mng_approve),
    path('mineral_mng_reject/<int:id>/',  views.mineral_mng_reject),

    #########################################################################################
    
    
    #### TEAM 3 ----> DEACETYLATION --> TEAM REPORTS,VIEW,APPROVE,DENY  

    ### TEAM 3 ----> REPORT PAGE & Detailed Report View
    path('deacetylation_report_page/',           views.deacetylation_report_page),
    path('deacetylationn_report_view/<int:id>/', views.deacetylationn_report_view),

    ## TEAM 3 ----> APPROVE & REJECT
    path('deacetylation_mng_approve/<int:id>/', views.deacetylation_mng_approve),
    path('deacetylation_mng_reject/<int:id>/',  views.deacetylation_mng_reject),
    
    ###########################################################################################


    #### TEAM 4 ----> CHITOSAN SYNTHESIS --> TEAM REPORTS,VIEW,APPROVE,DENY  

    #### TEAM 4 ----> REPORT PAGE & Detailed Report View
    path('chitosan_report_page/',          views.chitosan_report_page),
    path('chitosan_report_decryption/<int:id>/', views.chitosan_report_decryption),
    #
    # ## TEAM 4 ----> APPROVE & REJECT
    path('chitosan_mng_approve/<int:id>/', views.chitosan_mng_approve),
    path('chitosan_mng_reject/<int:id>/',  views.chitosan_mng_reject),
   
   ####################################################################################
   
   
    ## FINAL REPORT VIEW --> DOWNLOAD REPORT
    path('final_report_page/', views.final_report_page),
    path('view_final_report/<int:id>/', views.view_final_report, name='view_final_report'),



]
