from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
import random


from Manganese_Process.models import *
from Client.models import *
from App_Integration.models import *
from Porosity_Analysis.models import *

base_email = 'demosample47@gmail.com'
# MANAGER HOME PAGE
def manager_home_page(request):
    return render(request, 'Manager/manager_home.html')


# MANAGER LOGIN PAGE
def manager_login_page(request):
    if request.method =='POST':
        useremail = request.POST['useremail']
        password = request.POST['password']

        if useremail == "admin@gmail.com" and password == "admin":
            request.session['administrator'] = 'admin@gmail.com'
            messages.success(request, "Manager  logged in successfully")
            return redirect("/manager/manager_home/")

        elif useremail != "admin@gmail.com" and password == "admin":
            messages.error(request, "You have entered invalid email")
            return redirect('/manager/manager_login/')

        elif useremail == "admin@gmail.com" and password != "admin":
            messages.error(request, "You have entered wrong password")
            return redirect('/manager/manager_login/')

        elif useremail != "admin@gmail.com" and password != "admin":
            messages.error(request, "Invalid Credentials kinldy check")
            return redirect('/manager/manager_login/')

    return render(request,'Manager/login.html')


# MANAGER LOGOUT

def manager_login_out(request):
    if 'administrator' in request.session:
        print('If Block ')
        del request.session['administrator']
        messages.success(request, "Manager logged out successfully")
    else:
        print('Else Block')
        messages.info(request, "No user is currently logged in")

    return redirect('/')






# CLIENT LOGIN APPROVAL PAGE

def mg_app_login_client_view(request):
    datas = Client_register.objects.all()
    return render(request,'Manager/app_login_client.html',{'datas':datas})



def client_lg_approve_btn(request,id):
    if 'administrator' in request.session:
        values=Client_register.objects.get(id=id)
        values.cl_admin_lg=True #
        a = "CLI-"
        b = random.randint(1000,2000)
        c = str(a) + str(b)
        print(c)
        values.consumer_id=c
        values.save()
        messages.success(request,"Client details are verified and  approved, Client ID Genreated")
        return redirect("/manager/mg_app_login_client/")
    else:
        return redirect("/mg_app_login_client/")



def client_lg_reject_btn(request,id):
    if 'administrator' in request.session:
        values = Client_register.objects.get(id=id)
        values.delete()
        messages.success(request, "Client details are analyzed and access is denied")
        return redirect("/manager/mg_app_login_client/")
    else:
        return redirect("/manager/mg_app_login_client/")



 # **************

#  Manganese Page VIEW APPROVAl REJECT

def mg_app_login_mang_view(request):
    datas = Manganese_register.objects.all()
    return render(request,'Manager/app_login_manganese.html',{'datas':datas})




def manganese_login_approval(request,id):
    if 'administrator' in request.session:
        values=Manganese_register.objects.get(id=id)
        values.mg_admin_lg=True
        values.save()
        messages.success(request,"Managanese Team Details are Verified and  Approved")
        return redirect("/manager/mg_app_login_manganese/")
    else:
        return redirect("/manager/mg_app_login_manganese/")


def manganese_login_reject(request,id):
    if 'administrator' in request.session:
        values = Manganese_register.objects.get(id=id)
        values.delete()
        messages.success(request, "Manganese Team Details are Analyzed and Access is Denied")
        return redirect("/manager/mg_app_login_manganese/")
    else:
        return redirect("/manager/mg_app_login_manganese/")






# APPLICANT VIEW APPROVAL REJECT

def mg_app_login_application_view(request):
    datas = Application_register.objects.all()
    return render(request,'Manager/app_login_application.html',{'datas':datas})




def application_login_approval(request,id):
    if 'administrator' in request.session:
        values=Application_register.objects.get(id=id)
        values.app_admin_lg=True
        values.save()
        messages.success(request,"Applicant details are verified and  approved")
        return redirect("/manager/mg_app_login_application/")
    else:
        return redirect("/manager/mg_app_login_application/")


def application_login_reject(request,id):
    if 'administrator' in request.session:
        values = Application_register.objects.get(id=id)
        values.delete()
        messages.success(request, "Applicant details are analyzed and access is denied")
        return redirect("/manager/mg_app_login_application/")
    else:
        return redirect("/manager/mg_app_login_application/")






# POROSITY VIEW APPROVE DENY


def mg_app_login_porosity_view(request):
    datas = Porosity_register.objects.all()
    return render(request,'Manager/app_login_porosity.html',{'datas':datas})





def porosity_login_approval(request,id):
    if 'administrator' in request.session:
        values=Porosity_register.objects.get(id=id)
        values.por_admin_lg=True
        values.save()
        messages.success(request,"Porosity Team details are verified and approved")
        return redirect("/manager/mg_app_login_porosity/")
    else:
        return redirect("/manager/mg_app_login_porosity/")


def porosity_login_reject(request,id):
    if 'administrator' in request.session:
        values = Porosity_register.objects.get(id=id)
        values.delete()
        messages.success(request, "Porosity Team details are analyzed and access is denied")
        return redirect("/manager/mg_app_login_porosity/")
    else:
        return redirect("/manager/mg_app_login_porosity/")




##### CURRENTLY WORKING ###



# MANGANESE PROCESSED REPORT (3 VIEWS )


def mg_view_report(request):
    client_orders = Client_orders.objects.exclude(manganese_Comp__isnull=True)
    return render(request, 'Manager/b_mang_final_report_view.html', {'client_orders': client_orders})






def mg_view_report_mganalysis(request,id):
    mg_calculations = Client_orders.objects.get(id=id)
    return render(request, 'Manager/mang_final_report_mganalysis.html', {'mg_calculations': mg_calculations})



def mg_final_report_approve(request,id):
    final = Client_orders.objects.get(id=id)
    final.mang_admin_approve = True
    final.save()
    messages.success(request,'Successfully Manganese Team Report Approved By Manager')
    return redirect('/manager/mg_view_report/')





# APP INTEGRATION VIEW


def app_view_report(request):
    client_orders = Client_orders.objects.exclude(app_process=False)
    return render(request, 'Manager/d_app_final_report_view.html', {'client_orders': client_orders})



def app_view_Component(request,id):
    client_orders = Client_orders.objects.get(id=id)
    product = client_orders.product
    components = Components_required.objects.filter(product=product)
    return render(request, 'Manager/manager_final_component.html', {'components': components})


def app_final_report_approve(request,id):
    client_orders = Client_orders.objects.get(id=id)
    client_orders.app_admin_approve =True
    client_orders.save()
    messages.success(request,'Integration Report Approved by Manager')
    return redirect('/manager/app_view_report/')





# POROSITY TEAM REPORT VIEW AND APPROVE

def porosity_fin_report_view(request):
    client_orders = Client_orders.objects.filter(porosity_fin_report=True)
    return render(request, 'Manager/e_porosity_final_report_view.html', {'client_orders': client_orders})




def por_final_report_admin_approve(request,id):
    client_orders = Client_orders.objects.get(id=id)
    client_orders.por_rep_admin_approve =True
    client_orders.fintest = True
    client_orders.retest = False

    product = client_orders.product
    qnt     = client_orders.quantity

    price = {
        'Pressure Sensor': 120,
        'Battery': 75,
        'RRAM': 250,
        'Super Capacitors': 130,
    }
    total_price = int(price[product]) * int(qnt)
    client_orders.amount = total_price
    client_orders.save()

    messages.success(request,'Porosity Report Approved by Manager')
    return redirect('/manager/porosity_fin_report_view/')




def por_final_report_admin_reject(request, id):
    try:
        client_orders = Client_orders.objects.get(id=id)
        client_orders.fintest = False
        client_orders.retest = True
        client_orders.por_rep_admin_reject = True
        client_orders.save()
        Clientid = client_orders.consumer_id
        orderid = 'ORD10' + str(client_orders.id)

        subject = f"Conduct the Conductivity Test again and Improve the Conductivity Rate for Client ID: {Clientid} and Order ID: {orderid}"
        message = f"""
                Dear Porosity Test Team,
                After reviewing the Conductivity Test  for Client ID: {Clientid} and Order ID: {orderid}, we have identified a need to enhance conductivity.
                 As a result, I kindly request that the Porosity Test Team conduct the test again to improve the conductivity levels.
                If you have any questions or require further assistance, please do not hesitate to contact me.
                """

        from Porosity_Analysis.models import Porosity_register
        email_ids = list(Porosity_register.objects.values_list('email', flat=True))

        if email_ids:
            print("Email IDs found:", email_ids)
            recipients = email_ids
        else:
            print("No email IDs found, using base email ID")
            recipients = base_email

        send_mail(subject, message, from_email="new@example.com", recipient_list=recipients)
        print("Email sent successfully!")
        messages.success(request, 'Porosity Report Rejected by Manager')
    except Client_orders.DoesNotExist:
        messages.error(request, 'Client orders with provided ID does not exist')
    except Exception as e:
        # Handle any other exception (e.g., internet connection error, email sending failure)
        messages.success(request, 'Porosity Report Rejected by Manager')
        messages.error(request, f'An error occurred: {str(e)},It make because of Poor Internet')

    return redirect('/manager/porosity_fin_report_view/')






def payment_view(request):
    Order_payment = Client_orders.objects.filter(por_rep_admin_approve=True)
    return render(request,'Manager/g_payment_view.html',{'Order_payment':Order_payment})


def dispatch(request,id):
    dispatch_orders = Client_orders.objects.get(id=id)
    dispatch_orders.dispatch = True
    dispatch_orders.save()
    messages.success(request,'Successfully Dsipatched')
    return redirect('/manager/payment_view/')














