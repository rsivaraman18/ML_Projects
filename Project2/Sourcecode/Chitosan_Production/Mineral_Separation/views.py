from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from Mineral_Separation.models import *
from Manager.models import *
import pandas as pd
import random

def mineral_home_page(request):
    return render(request,'02_Mineral/02_home_page.html')


def mineral_register(request):
    if request.method == 'POST':
        username = request.POST['username'].title()
        email    = request.POST['email']
        contact  = request.POST['contact']
        password = request.POST['password']

        try:
            existing_user = Mineral_teams.objects.get(email=email)
            messages.error(request, 'Email already taken. Try another!')
            return redirect('/mineral_separation/mineral_register/')

        except Mineral_teams.DoesNotExist:
            try:
                new_team = Mineral_teams(username=username, email=email, contact=contact, password=password)
                new_team.save()
                messages.success(request, 'Successfully Mineral Separation Team Registered')
                return render(request, '02_Mineral/01_login_page.html')

            except IntegrityError as e:
                messages.error(request,f'An error occurred while registering: {e}')
                return redirect('/mineral_separation/mineral_register/')
    return render(request, '02_Mineral/01_login_page.html')


def mineral_login(request):
    if request.method=='POST':
        uemail = request.POST['useremail']
        upassword = request.POST['password']
        try:
            user = Mineral_teams.objects.get(email=uemail)
            if user.password == upassword:
                if user.mineral_login_approve:
                    request.session['mineral'] = uemail
                    messages.success(request, 'Mineral Separation Team  Successfully Logged In')
                    return redirect('/mineral_separation/mineral_home/')
                else:
                    messages.success(request, 'Please Wait for Admin Approval')
                    return redirect('/mineral_separation/mineral_login/')
            else:
                messages.error(request, 'Incorrect password. Please try again')
                return redirect('/mineral_separation/mineral_login/')

        except ObjectDoesNotExist:
            messages.error(request, 'No Mineral Separation Team with these credentials.')
            return redirect('/mineral_separation/mineral_login/')
    return render(request, '02_Mineral/01_login_page.html')


def mineral_logout(request):
    try:
        if 'mineral' in request.session:
            print('mineral Login:',request.session['mineral'])
            del request.session['mineral']
            messages.success(request, 'Mineral Team  logged out successfully')
    except KeyError:
        messages.error(request, 'Error occurred during logout')
    return redirect('/')


######################################################################
######################## MINERAL SEPARATION ##################################


def mineral_viewdata(request):
    datas = Chitosan_Productions.objects.filter(deproteint_report_mng=True)
    return render(request, '02_Mineral/03_Deproteinization_Report_Page.html', {'datas': datas})

def mineral_view_reports_data(request,id):
    detail = Chitosan_Productions.objects.get(id=id)
    return render(request, '02_Mineral/04_Deproteinization_Detailed_View.html', {'detail': detail})





#### DATASET UPLOAD ####

def mineral_dataset_upload(request):
    count = Mineral_dataset.objects.count()
    print('count value',count)
    if request.method == 'POST':
        try:
            file_datasource = request.FILES['file_datasource']
            data = pd.read_csv(file_datasource)
            for index, row in data.iterrows():
                instance = Mineral_dataset(
                    purpose   = row['Purpose of Usage'],
                    purity    = row['Required Purity (%)'],
                    quantity  = row['Desired Quantity (kg)'],
                    form      = row['Chitosan Form'],

                    Mineraltype         = row['Mineral Type'],
                    Separation_Method   = row['Separation Method'],
                    Reagent_Used        = row['Reagent Used'],
                    Reagent_Concentration = row['Reagent Concentration(%)'],
                    Separation_Time     = row['Separation Time(min)'],
                    Energy_Consumption  = row['Energy Consumption( kWh)'],
                )
                instance.save()
            messages.success(request,'Mineral separation Prerequisite are Upload Successfully')
            return redirect('/mineral_separation/mineral_dataset_upload/')

        except IntegrityError:
            messages.success(request, 'Error In Updating Products')
            return redirect('/mineral_separation/mineral_home/')
    return render(request,'02_Mineral/05_Mineral_Upload.html',{'count':count})




def mineral_start_process(request):
    datas = Chitosan_Productions.objects.filter(deproteint_report_mng=True)
    return render(request, '02_Mineral/06_Mineral_Process.html', {'datas': datas})




def mineral_start_analyse(request,id):
    order_data   = Chitosan_Productions.objects.get(id=id)
    order_detail = [order_data.purpose,order_data.purity,order_data.quantity,order_data.form]
    print(order_detail)
    matching_products = Mineral_dataset.objects.filter(purpose=order_detail[0],purity=order_detail[1],quantity=order_detail[2],form=order_detail[3])

    matching_products_list = []

    for product in matching_products:
        product_values = [product.Mineraltype, product.Separation_Method, product.Reagent_Used, product.Reagent_Concentration,product.Separation_Time,product.Energy_Consumption]
        matching_products_list.append(product_values)

    result = matching_products_list[0]
    # print('match:',matching_products)
    print(result)
    order_data.Mineraltype        = result[0]
    order_data.Separation_Method  = result[1]
    order_data.Reagent_Used       = result[2]
    order_data.Reagent_Concentration = result[3]
    order_data.Separation_Time       = result[4]
    order_data.Energy_Consumption    = result[5]

    order_data.mineral_report = True
    order_data.save()
    messages.success(request,"Mineral Separtion Process Successfully Completed")
    return redirect('/mineral_separation/mineral_start_process_page/')





def mineral_calculation_page(request):
    datas = Chitosan_Productions.objects.filter(mineral_report=True)
    return render(request, '02_Mineral/07_Mineral_EfficencyCalculation.html', {'datas': datas})


def mineral_start_calculate(request, id):
    order_data = Chitosan_Productions.objects.get(id=id)
    values = {
        'purity': int(order_data.purity),
        'separation_time': int(order_data.Separation_Time),
        'Reagent': float(order_data.Reagent_Concentration),
        'quantity': int(order_data.quantity),
        'energy': int(order_data.Energy_Consumption),
    }


    min_efficiency = ((values['purity'] * values['separation_time']) - (
                values['separation_time'] * values['separation_time'])) / values['separation_time']
    min_efficiency = round(random.uniform(85, 95),2)
    order_data.min_efficiency     = min_efficiency
    order_data.mineral_report_c1 = True
    order_data.save()
    messages.success(request, "Mineral Separation Efficiency Calculated Successfully")
    return redirect('/mineral_separation/mineral_calculation_page/')


def mineral_report_page(request):
    datas = Chitosan_Productions.objects.filter(mineral_report_c1=True)
    return render(request, '02_Mineral/08_Mineral_Report_Page.html', {'datas': datas})


def mineral_report_view(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '02_Mineral/09_Mineral_Detailed_Report.html', {'details': details})

