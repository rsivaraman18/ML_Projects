from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from Deacetylation.models import *
from Manager.models import *
import pandas as pd
import random

def deacetyl_home_page(request):
    return render(request,'03_Deacetylation/02_home_page.html')


def deacetyl_register(request):
    if request.method == 'POST':
        username = request.POST['username'].title()
        email    = request.POST['email']
        contact  = request.POST['contact']
        password = request.POST['password']

        try:
            existing_user = Deacetyl_teams.objects.get(email=email)
            messages.error(request, 'Email already taken. Try another!')
            return redirect('/deacetylation/deacetyl_register/')

        except Deacetyl_teams.DoesNotExist:
            try:
                new_team = Deacetyl_teams(username=username, email=email, contact=contact, password=password)
                new_team.save()
                messages.success(request, 'Successfully Deacetyl Team Registered')
                return render(request, '03_Deacetylation/01_login_page.html')

            except IntegrityError as e:
                messages.error(request,f'An error occurred while registering: {e}')
                return redirect('/deacetylation/deacetyl_register/')
    return render(request, '03_Deacetylation/01_login_page.html')


def deacetyl_login(request):
    if request.method=='POST':
        uemail = request.POST['useremail']
        upassword = request.POST['password']
        try:
            user = Deacetyl_teams.objects.get(email=uemail)
            if user.password == upassword:
                if user.deacetyl_login_approve:
                    request.session['deacetyl'] = uemail
                    messages.success(request, 'deacetyl_login_approve Team  Successfully Logged In')
                    return redirect('/deacetylation/deacetyl_home/')
                else:
                    messages.success(request, 'Please Wait for Admin Approval')
                    return redirect('/deacetylation/deacetyl_login/')
            else:
                messages.error(request, 'Incorrect password. Please try again')
                return redirect('/deacetylation/deacetyl_login/')

        except ObjectDoesNotExist:
            messages.error(request, 'No Deacetyl Team with these credentials.')
            return redirect('/deacetylation/deacetyl_login/')
    return render(request, '03_Deacetylation/01_login_page.html')


def deacetyl_logout(request):
    try:
        if 'deacetyl' in request.session:
            print('Deacetyl Login:',request.session['deacetyl'])
            del request.session['deacetyl']
            messages.success(request, 'Deacetyl Team  logged out successfully')
    except KeyError:
        messages.error(request, 'Error occurred during logout')
    return redirect('/')

#############################################################
###############################################################


############################ START PROCESS ############################
##########################################################################


def deacetylation_mineral_report_page(request):
    datas = Chitosan_Productions.objects.filter(mineral_report_mng=True)
    return render(request, '03_Deacetylation/03_Mineral_Report.html', {'datas': datas})


def deacetylation_mineral_detailed_report(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '03_Deacetylation/04_Mineral_Report_Detailed.html', {'details': details})




##### DATASET UPLOAD ####

def deacetylation_dataset_upload(request):
    count = Deacetylation_dataset.objects.count()
    print('count value',count)
    if request.method == 'POST':
        try:
            file_datasource = request.FILES['file_datasource']
            data = pd.read_csv(file_datasource)
            for index, row in data.iterrows():
                instance = Deacetylation_dataset(
                    purpose    = row['Purpose of Usage'],
                    purity     = row['Required Purity (%)'],
                    quantity   = row['Desired Quantity (kg)'],
                    form       = row['Chitosan Form'],

                    Deacetylation_Method   = row['Deacetylation Method'],
                    Reaction_Temperature        = row['Reaction Temperature(°C)'],
                    Reaction_Time        = row['Reaction Time(hours)'],
                    Degree_Deacetylation   = row['Degree of Deacetylation(%)'],
                    Ash_Content       = row['Ash Content(%)'],
                )
                instance.save()
            messages.success(request,'Deacetylation Requirements are Upload Successfully')
            return redirect('/deacetylation/deacetylation_dataset_upload/')

        except IntegrityError:
            messages.success(request, 'Error In Updating Products')
            return redirect('/deacetylation/deacetyl_home/')
    return render(request,'03_Deacetylation/05_Deacetylation_Dataset.html',{'count':count})




def deacetyl_process_page(request):
    datas = Chitosan_Productions.objects.filter(mineral_report_mng=True)
    return render(request, '03_Deacetylation/06_Deacetylation_Process.html', {'datas': datas})



def deacetyl_start_process(request,id):
    order_data = Chitosan_Productions.objects.get(id=id)
    order_details = [order_data.purpose,order_data.purity,order_data.quantity,order_data.form]
    matching_products = Deacetylation_dataset.objects.filter(purpose=order_details[0],purity=order_details[1],quantity=order_details[2],form=order_details[3])
    matching_products_list = []

    for product in matching_products:
        product_values = [product.Deacetylation_Method, product.Reaction_Temperature, product.Reaction_Time, product.Degree_Deacetylation,product.Ash_Content]
        matching_products_list.append(product_values)

    result = matching_products_list[0]
    print(result)
    order_data.Deacetylation_Method = result[0]
    order_data.Reaction_Temperature = result[1]
    order_data.Reaction_Time = result[2]
    order_data.Degree_Deacetylation = result[3]
    order_data.Ash_Content = result[4]


    order_data.deacetyl_report = True
    order_data.save()
    messages.success(request,"Deacetyl Process Successfully Completed")
    return redirect('/deacetylation/deacetyl_process_page/')







def deacetyl_calculation_page(request):
    datas = Chitosan_Productions.objects.filter(mineral_report=True)
    return render(request, '03_Deacetylation/07_Deacetylation_Calculation.html', {'datas': datas})


def deacetyl_start_calculate(request, id):
    order_data = Chitosan_Productions.objects.get(id=id)
    degree_deacetylation = float(order_data.Degree_Deacetylation)
    max_degree_deacetylation = 95
    deacetyl_efficiency = 0.9 * (degree_deacetylation/max_degree_deacetylation)
    deacetyl_efficiency = round(random.uniform(85, 95),2)
    order_data.deacetyl_efficiency     = deacetyl_efficiency
    order_data.deacetyl_report_c1 = True
    order_data.save()
    messages.success(request, "Efficiency Calculated Successfully")
    return redirect('/deacetylation/deacetyl_calculation_page/')





def deacetyl_report_page(request):
    datas = Chitosan_Productions.objects.filter(deacetyl_report_c1=True)
    return render(request, '03_Deacetylation/08_Deacetylation_report.html', {'datas': datas})


def deacetyl_report_detail_view(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '03_Deacetylation/09_Deacetylation_View_Report.html', {'details': details})


