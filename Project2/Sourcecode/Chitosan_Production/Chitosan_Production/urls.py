
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),

    ### This will Call the Project Views.py Code
    path('', views.home_view, name='home'),

    ### This will call the Urls.py code in App Level


    path('deproteinization/',   include('Deproteinization.urls')),
    path('mineral_separation/', include('Mineral_Separation.urls')),
    path('deacetylation/',      include('Deacetylation.urls')),
    path('chitosan_synthesis/', include('Chitosan_Synthesis.urls')),
    path('manager/',            include('Manager.urls')),
    #

]
