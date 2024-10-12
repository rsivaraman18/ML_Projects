from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from Deproteinization.models import *
from Manager.models import *
import pandas as pd

def deprotein_home_page(request):
    return render(request,'01_Deproteinization/02_Home_page.html')


def deprotein_register(request):
    if request.method == 'POST':
        username = request.POST['username'].title()
        email    = request.POST['email']
        contact  = request.POST['contact']
        password = request.POST['password']

        try:
            existing_user = Deprotein_teams.objects.get(email=email)
            messages.error(request, 'Email already taken. Try another!')
            return redirect('/deproteinization/deprotein_register/')

        except Deprotein_teams.DoesNotExist:
            try:
                new_team = Deprotein_teams(username=username, email=email, contact=contact, password=password)
                new_team.save()
                messages.success(request, 'Successfully Deproteinization Team Registered')
                return render(request, '01_Deproteinization/01_login_page.html')

            except IntegrityError as e:
                messages.error(request,f'An error occurred while registering: {e}')
                return redirect('/deproteinization/deprotein_register/')
    return render(request, '01_Deproteinization/01_login_page.html')


def deprotein_login(request):
    if request.method=='POST':
        uemail = request.POST['useremail']
        upassword = request.POST['password']
        try:
            user = Deprotein_teams.objects.get(email=uemail)
            if user.password == upassword:
                if user.deprotein_login_approve:
                    request.session['Deproteinization'] = uemail
                    messages.success(request, 'Deproteinization Team  Successfully Logged In')
                    return redirect('/deproteinization/deprotein_home/')
                else:
                    messages.success(request, 'Please Wait for Admin Approval')
                    return redirect('/deproteinization/deprotein_login/')
            else:
                messages.error(request, 'Incorrect password. Please try again')
                return redirect('/deproteinization/deprotein_login/')

        except ObjectDoesNotExist:
            messages.error(request, 'No Deproteinization Team with these credentials.')
            return redirect('/deproteinization/deprotein_login/')
    return render(request, '01_Deproteinization/01_login_page.html')


def deprotein_logout(request):
    try:
        if 'Deproteinization' in request.session:
            print('Deproteinization Login:',request.session['Deproteinization'])
            del request.session['Deproteinization']
            messages.success(request, 'Deproteinization Team  logged out successfully')
    except KeyError:
        messages.error(request, 'Error occurred during logout')
    return redirect('/')



#################################### PROCESS CODING BEGINS



##################### PROCESSS STARTS
##################################################################


def deproteinization_viewdata(request):
    datas = Chitosan_Productions.objects.all()
    return render(request,'01_Deproteinization/03_View_New_Requirements_Page.html',{'datas':datas})

def deproteinization_detailed_data(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '01_Deproteinization/04_View_Requirement_Details.html', {'details': details})


import pandas as pd

def deproteinization_dataset_upload(request):
    count = Deprotein_dataset.objects.count()
    print('count value',count)
    if request.method == 'POST':

        try:
            print('Ready to Upload')
            file_datasource = request.FILES['file_datasource']
            data = pd.read_csv(file_datasource)
            for index, row in data.iterrows():
                instance = Deprotein_dataset(
                    purpose  = row['Purpose of Usage'],
                    purity = row['Required Purity (%)'],
                    quantity  = row['Desired Quantity (kg)'],
                    form  = row['Chitosan Form'],
                    Shell_Type  = row['Shell Type'],
                    Processing_Method  = row['Processing Method'],
                    NaOH_Concentration  = row['NaOH Concentration'],
                    Treatment_Time  = row['Treatment Time(hrs)'],
                    Moisture_Loss  = row['Moisture Loss(%)'],
                    NaOH_Quantity  = row['NaOH Quantity(Litres)'],

                )
                instance.save()

            messages.success(request,'Deproteinization Prerequisite are  Upload Successfully')
            return redirect('/deproteinization/deproteimization_dataset_upload/')

        except IntegrityError:
            messages.success(request, 'Error In Updating ')
            return redirect('')
    return render(request,'01_Deproteinization/05_Chitosan_Prerequisite.html',{'count':count})




def deproteinization_start_process(request):
    datas = Chitosan_Productions.objects.all()
    return render(request, '01_Deproteinization/06_Calulated_Analysis.html', {'datas': datas})


def deproteinization_start_analyse(request,id):
    requirement = Chitosan_Productions.objects.get(id=id)
    requirement_details = [requirement.purpose, requirement.purity, requirement.quantity,requirement.form ]
    print('requirement_details',requirement_details)
    matching_products = Deprotein_dataset.objects.filter(purpose=requirement_details[0],purity=requirement_details[1],quantity=requirement_details[2],form=requirement_details[3])


    matching_products_list = []

    for product in matching_products:
        product_values = [product.Shell_Type, product.Processing_Method, product.NaOH_Concentration, product.Treatment_Time,product.Moisture_Loss,product.NaOH_Quantity]
        matching_products_list.append(product_values)

    result = matching_products_list[0]
    print("matching 2:",matching_products_list)


    print(result)
    requirement.Shell_Type         = result[0]
    requirement.Processing_Method  = result[1]
    requirement.NaOH_Concentration = result[2]
    requirement.Treatment_Time     = result[3]
    requirement.Moisture_Loss      = result[4]
    requirement.NaOH_Quantity      = result[5]

    requirement.deprotein_report = True
    requirement.save()

    messages.success(request,"Deprotein Analysis Done")
    return redirect('/deproteinization/start_process_page/')



def deproteinization_report_page(request):
    datas = Chitosan_Productions.objects.filter(deprotein_report=True)
    return render(request, '01_Deproteinization/07_Deproteinization_Report_Page.html', {'datas': datas})


def deproteinization_report_view(request,id):
    data = Chitosan_Productions.objects.get(id=id)
    return render(request, '01_Deproteinization/08_Deproteinization_Report_view.html', {'data': data})

