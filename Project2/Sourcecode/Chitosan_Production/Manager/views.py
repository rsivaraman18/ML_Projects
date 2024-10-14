from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

import random
from Deproteinization.models import *
from Mineral_Separation.models import *
from Deacetylation.models import *
from Chitosan_Synthesis.models import *
from Manager.models import *


# MANAGER HOME PAGE
def manager_home_page(request):
    return render(request, '05_Manager/02_Home.html')


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

    return render(request,'05_Manager/01_Login.html')


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


#####################################################
#####################################################
# MODULE 1
####### Deproteinzation ACCESS PAGE ############
#### Deproteinization ACCESS,ID GENERATION,DENY.


def manager_dep_access_page(request):
    datas = Deprotein_teams.objects.all()
    return render(request,'05_Manager/03_Access_Deprotein.html',{'datas':datas})




def manager_dep_access_approve(request,id):
    if 'administrator' in request.session:
        user = Deprotein_teams.objects.get(id=id)
        clientids    = Deprotein_teams.objects.values_list('deprotein_team_id',flat=True)
        clientidlist = list(clientids)
        maximum_value = 0
        old_ids = []
        for id in clientidlist:
            if id !=None:
                new = int(id[-4:])
                old_ids.append(new)
        if not old_ids:
            maximum_value = 1000
        else:
            maximum_value = max(old_ids)

        new_id = maximum_value + 1
        gen_id = "DEP"+ str(new_id)
        user.deprotein_login_approve = True
        user.deprotein_team_id = gen_id
        user.save()
        messages.success(request, "Congratulations! Your ID has been successfully activated")
        return redirect('/manager/manager_dep_access_page/')

    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect('/manager/manager_dep_access_page/')



def manager_dep_access_deny(request,id):
    if 'administrator' in request.session:
        users = Deprotein_teams.objects.get(id=id)
        users.delete()
        messages.success(request, "Deproteinization Team access denied by Manager")
        return redirect('/manager/manager_dep_access_page/')
    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect("/manager/manager_dep_access_page/")


##################################################################



# MODULE 2
####### MINERAL SEPARATION ACCESS PAGE ############
#### MINERAL ACCESS,ID GENERATION,DENY.


def manager_mineral_access_page(request):
    datas = Mineral_teams.objects.all()
    return render(request,'05_Manager/04_Access_Mineral.html',{'datas':datas})




def manager_mineral_access_approve(request,id):
    if 'administrator' in request.session:
        user = Mineral_teams.objects.get(id=id)
        clientids    = Mineral_teams.objects.values_list('mineral_team_id',flat=True)
        clientidlist = list(clientids)
        maximum_value = 0
        old_ids = []
        for id in clientidlist:
            if id !=None:
                new = int(id[-4:])
                old_ids.append(new)
        if not old_ids:
            maximum_value = 1000
        else:
            maximum_value = max(old_ids)

        new_id = maximum_value + 1
        gen_id = "MIN"+ str(new_id)
        user.mineral_login_approve = True
        user.mineral_team_id = gen_id
        user.save()
        messages.success(request, "Congratulations! New ID Generated")
        return redirect('/manager/manager_mineral_access_page/')

    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect('/manager/manager_mineral_access_page/')



def manager_mineral_access_deny(request,id):
    if 'administrator' in request.session:
        users = Mineral_teams.objects.get(id=id)
        users.delete()
        messages.success(request, "Mineral Separation Team access denied by Manager")
        return redirect('/manager/manager_mineral_access_page/')
    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect("/manager/manager_mineral_access_page/")


##################################################################
#####################


# MODULE 3 DEACETYLATION
####### DEACETYLATION ACCESS PAGE ############
#### DEACETYLATION ACCESS,ID GENERATION,DENY.


def manager_deacetyl_access_page(request):
    datas = Deacetyl_teams.objects.all()
    return render(request,'05_Manager/05_Access_Deacetyl.html',{'datas':datas})




def manager_deacetyl_access_approve(request,id):
    if 'administrator' in request.session:
        user = Deacetyl_teams.objects.get(id=id)
        clientids    = Deacetyl_teams.objects.values_list('deacetyl_team_id',flat=True)
        clientidlist = list(clientids)
        maximum_value = 0
        old_ids = []
        for id in clientidlist:
            if id !=None:
                new = int(id[-4:])
                old_ids.append(new)
        if not old_ids:
            maximum_value = 1000
        else:
            maximum_value = max(old_ids)

        new_id = maximum_value + 1
        gen_id = "DEC"+ str(new_id)
        user.deacetyl_login_approve = True
        user.deacetyl_team_id = gen_id
        user.save()
        messages.success(request, "Your ID has been successfully activated")
        return redirect('/manager/manager_deacetyl_access_page/')

    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect('/manager/manager_deacetyl_access_page/')



def manager_deacetyl_access_deny(request,id):
    if 'administrator' in request.session:
        users = Deacetyl_teams.objects.get(id=id)
        users.delete()
        messages.success(request, "Deacetyl Team access denied by Manager")
        return redirect('/manager/manager_deacetyl_access_page/')
    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect("/manager/manager_deacetyl_access_page/")


##################################################################
#####################


# MODULE 4
####### CHITOSAN ACCESS PAGE ############
#### CHITOSAN ACCESS,ID GENERATION,DENY.


def manager_chitosan_access_page(request):
    datas = Chitosan_teams.objects.all()
    return render(request,'05_Manager/06_Access_Chitosan.html',{'datas':datas})




def manager_chitosan_access_approve(request,id):
    if 'administrator' in request.session:
        user = Chitosan_teams.objects.get(id=id)
        clientids    = Chitosan_teams.objects.values_list('chitosan_team_id',flat=True)
        clientidlist = list(clientids)
        maximum_value = 0
        old_ids = []
        for id in clientidlist:
            if id !=None:
                new = int(id[-4:])
                old_ids.append(new)
        if not old_ids:
            maximum_value = 1000
        else:
            maximum_value = max(old_ids)

        new_id = maximum_value + 1
        gen_id = "VIT"+ str(new_id)
        user.chitosan_login_approve = True
        user.chitosan_team_id = gen_id
        user.save()
        messages.success(request, " Your ID has been successfully activated")
        return redirect('/manager/manager_chitosan_access_page/')

    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect('/manager/manager_chitosan_access_page/')



def manager_chitosan_access_deny(request,id):
    if 'administrator' in request.session:
        users = Chitosan_teams.objects.get(id=id)
        users.delete()
        messages.success(request, "Chitosan Team access denied by Manager")
        return redirect('/manager/manager_chitosan_access_page/')
    else:
        messages.success(request, 'Error in your Session. Please log in again')
        return redirect("/manager/manager_chitosan_access_page/")


########################################################################
###################
### UPLOAD PAAGE AND NEW UPLOAD


def manager_upload_requirement_page(request):
    datas = Chitosan_Productions.objects.all()
    return render(request, '05_Manager/07_Upload_Chitosan_Required.html', {'datas': datas})


def manager_upload_new_requirement(request):
    if request.method=="POST":
        try:
            name     = request.POST['uname'].title()
            purpose  = request.POST['Purpose_of_Usage']
            purity   = request.POST['Required_Purity']
            quantity = request.POST['Desired_Quantity']
            form     = request.POST['Chitosan_Form']

            patient = Chitosan_Productions(name=name, purpose=purpose, purity=purity, quantity=quantity ,form=form )
            patient.save()
            messages.success(request,'New Chitosan Requirements Upload Successfully')
            print('Saved Done')
        except:
            messages.success(request,'Error in Updating New Entries')
        return redirect('/manager/manager_upload_requirement_page/')
    return render(request, '05_Manager/08_Upload_New_Requirement.html')






###################################################################################
####################################################################################

##################### ############## ###################
######################## MODULE -1 REPORT VIEW APPROVE DENY #######

def deproteinization_report_page(request):
    datas = Chitosan_Productions.objects.filter(deprotein_report=True)
    return render(request, '05_Manager/09_Dep_Manager_Page.html', {'datas': datas})


def deproteinization_report_view(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '05_Manager/10_Dep_Report_View.html', {'details': details})




def deproteinization_report_mng_approve(request,id):
    if 'administrator' in request.session:
        values=Chitosan_Productions.objects.get(id=id)
        values.deproteint_report_mng=True
        values.save()
        messages.success(request,"Deproteinization Team Reports are approved by Manager")
        return redirect("/manager/deproteinization_report_page/")
    else:
        return redirect("/manager/deproteinization_report_page/")


def deproteinization_report_mng_reject(request,id):
    if 'administrator' in request.session:
        values = Chitosan_Productions.objects.get(id=id)
        values.delete()
        messages.success(request, "Deproteinization Team Reports are rejected by Manager")
        return redirect("/manager/deproteinization_report_page/")
    else:
        return redirect("/manager/deproteinization_report_page/")


##################################################

##################### ############## ###################
######################## MODULE -2 REPORT VIEW APPROVE DENY #######

def mineral_report_page(request):
    datas = Chitosan_Productions.objects.filter(mineral_report_c1=True)
    return render(request, '05_Manager/11_Mineral_separation_report.html', {'datas': datas})


def mineral_report_view(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '05_Manager/12_Mineral_Detailed_report.html', {'details': details})



def mineral_mng_approve(request,id):
    if 'administrator' in request.session:
        values=Chitosan_Productions.objects.get(id=id)
        values.mineral_report_mng=True
        values.save()
        messages.success(request,"Mineral Separation Reports are approved by Manager")
        return redirect("/manager/mineral_report_page/")
    else:
        return redirect("/manager/mineral_report_page/")


def mineral_mng_reject(request,id):
    if 'administrator' in request.session:
        values = Chitosan_Productions.objects.get(id=id)
        values.delete()
        messages.success(request, "Mineral Separation Team Reports are rejected by Manager")
        return redirect("/manager/mineral_report_page/")
    else:
        return redirect("/manager/mineral_report_page/")


##################################################


##################### ############## ###################
######################## MODULE -3 REPORT VIEW APPROVE DENY #######
##

def deacetylation_report_page(request):
    datas = Chitosan_Productions.objects.filter(deacetyl_report_c1=True)
    return render(request, '05_Manager/13_Deacetylation_Report.html', {'datas': datas})


def deacetylationn_report_view(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '05_Manager/14_Deacetylation_Report_View.html', {'details': details})




def deacetylation_mng_approve(request,id):
    if 'administrator' in request.session:
        values=Chitosan_Productions.objects.get(id=id)
        values.deacetyl_report_mng=True
        values.save()
        messages.success(request,"Deacetylation Team Reports are approved by Manager")
        return redirect("/manager/deacetylation_report_page/")
    else:
        return redirect("/manager/deacetylation_report_page/")


def deacetylation_mng_reject(request,id):
    if 'administrator' in request.session:
        values = Chitosan_Productions.objects.get(id=id)
        values.delete()
        messages.success(request, "Deacetylation Team Reports are rejected by Manager")
        return redirect("/manager/deacetylation_report_page/")
    else:
        return redirect("/manager/deacetylation_report_page/")


##################################################



##################### ############## ###################
######################## MODULE -4 REPORT VIEW APPROVE DENY #######



def chitosan_report_page(request):
    datas = Chitosan_Productions.objects.filter(chitosan_report=True, chitosan_encrypt=True,key_sent=True)
    return render(request, '05_Manager/15_Chitosan_Report.html', {'datas': datas})

#############################################BLOACK CHAIN VIEW #################

import hashlib
import json
from time import time
from cryptography.fernet import Fernet
import base64

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time(), [], "0", 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block):
        block.hash = block.compute_hash()
        self.chain.append(block)

    @property
    def last_block(self):
        return self.chain[-1]

    def new_block(self, transactions, proof):
        block = Block(
            index=len(self.chain),
            timestamp=time(),
            transactions=transactions,
            previous_hash=self.last_block.compute_hash(),
            proof=proof,
        )
        return block

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


def chitosan_report_decryption(request, id):
    data        = Chitosan_Productions.objects.get(id=id)
    orginal_key = data.encryption_key

    report = {
        'chitosan_extract_method': data.encrypted_chitosan_extract_method,
        'chit_reagent': data.encrypted_chit_reagent,
        'viscosity': data.encrypted_viscosity,
        'chit_reagent_concentration': data.encrypted_chit_reagent_concentration,
        'chitosan_efficiency': data.encrypted_chitosan_efficiency,
    }

    if request.method=='POST':
        user_key = request.POST.get('user_key')
        if user_key == orginal_key:
            try:
                key_bytes = base64.urlsafe_b64decode(user_key.encode('utf-8'))

                fernet = Fernet(key_bytes)
                decrypted_report = {}
                blockchain = Blockchain()

                stored_block_hash = data.block_hash
                current_block = blockchain.new_block(
                    {
                        'chitosan_extract_method': data.encrypted_chitosan_extract_method,
                        'chit_reagent': data.encrypted_chit_reagent,
                        'viscosity': data.encrypted_viscosity,
                        'chit_reagent_concentration': data.encrypted_chit_reagent_concentration,
                        'chitosan_efficiency': data.encrypted_chitosan_efficiency,
                    }, blockchain.last_block.proof)

                for field in ['chitosan_extract_method', 'chit_reagent', 'viscosity', 'chit_reagent_concentration',
                              'chitosan_efficiency']:
                    encrypted_value = getattr(data, f"encrypted_{field}")
                    try:
                        decrypted_value = fernet.decrypt(encrypted_value.encode()).decode('utf-8')
                        decrypted_report[field] = decrypted_value
                    except Exception:
                        decrypted_report[field] = encrypted_value
                print('try Block Decrypted Successfully')
                print(decrypted_report)
                print('Encrypted Key Matches Fetching Exact Data')
                return render(request, '05_Manager/16_Chitosan_Report_Detailed.html',
                              {'report': decrypted_report, 'key': True, 'id': id})

            except:
                print('Except Block ')
                report = {'chitosan_extract_method': data.chitosan_extract_method, 'chit_reagent': data.chit_reagent,
                          'viscosity': data.viscosity, 'chit_reagent_concentration ': data.chit_reagent_concentration,
                          'chitosan_efficiency': data.chitosan_efficiency, }
                return render(request, '05_Manager/16_Chitosan_Report_Detailed.html',
                              {'report': report, 'key': True, 'id': id})

        messages.success(request, "Encryption Key Mismatch")
        return redirect('/manager/chitosan_report_page/')

    return render(request, '05_Manager/16_Chitosan_Report_Detailed.html', {'report': report,'key':False,'id':id})







# ##################################### PDF GENERATION FUNCTION AND APPROVAL CODE#################

# ##################################### PDF GENERATION FUNCTION AND APPROVAL CODE#################

from django.shortcuts import redirect
from django.contrib import messages
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from django.core.files.storage import default_storage
from PyPDF2 import PdfReader, PdfWriter
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def image_pdf(data, pname, pid):
    # Create a graph using matplotlib
    fig, ax = plt.subplots()
    x = np.arange(1, 5)  # X-axis values (e.g., categories 1 through 4)
    values = [data.Moisture_Loss, data.min_efficiency, data.deacetyl_efficiency,
              data.chitosan_efficiency]

    # Plotting with a curve
    ax.plot(x, values, marker='o', linestyle='-', color='b')

    # Adding labels and title
    ax.set_xticks(x)
    ax.set_xticklabels(['Moisture Loss', 'Mineral Separation', 'Deacetylation', 'Chitosan Synthesis'])
    ax.set_xlabel('Efficiency')
    ax.set_ylabel('Values')
    ax.set_title('Efficiency Statistics')

    # Adding grid for better visibility
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Save the graph image
    graph_buffer = BytesIO()
    plt.savefig(graph_buffer, format='png')
    plt.close(fig)
    graph_buffer.seek(0)

    # Save the graph image to storage
    graph_filename = pname + pid + '_graph.png'
    graph_path = os.path.join(BASE_DIR, 'Graphs', graph_filename)
    with default_storage.open(graph_path, 'wb') as graph_file:
        graph_file.write(graph_buffer.getvalue())

    # Update database with graph image path
    data.Image_graph = graph_path
    data.save()

    return graph_path


def generate_pdf(id):
    data = Chitosan_Productions.objects.get(id=id)
    pname = data.name
    pid = '100' + str(data.id)
    filename = pname + pid + '.pdf'
    password = pname + pid

    # Create a PDF document
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Table 1: Client Details
    clienttable = [['NAME', 'CLIENT ID', 'PURPOSE', 'PURITY', 'QUANTITY','FORM']]
    client1 = [data.name, data.id, data.purpose, data.purity + ' %', data.quantity + ' kg',data.form]
    clienttable.append(client1)

    styles = getSampleStyleSheet()
    table_name_style = styles['Title']

    # Table 1 Title
    table1_name = Paragraph("<b>CLIENT DETAILS</b>", table_name_style)
    elements.append(table1_name)

    table1 = Table(clienttable)
    table1.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightskyblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table1)
    elements.append(Spacer(1, 45))

    # Table 2: Module 2 Report
    gemtable = [["S.NO", "CONTENT", "DETAILS"]]
    gems = [
        (1, 'Shell Type', data.Shell_Type ),
        (2, 'Processing Method', data.Processing_Method ),
        (3, 'NaOH Concentration', data.NaOH_Concentration   ),
        (4, 'Treatment Time', data.Treatment_Time + ' hrs'),
        (5, 'Moisture Loss', data.Moisture_Loss + ' %'),
        (6, 'NaOH Quantity', data.NaOH_Quantity + ' Litres'),
    ]
    for gem in gems:
        gemtable.append(gem)

    table2 = Table(gemtable)
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightskyblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    table2_name = Paragraph("<b>DEPROTEINIZATION REPORT</b>", table_name_style)
    elements.append(table2_name)
    elements.append(table2)
    elements.append(Spacer(1, 45))

    # Table 3: Module 3 Report
    cotable = [['S.No', 'CONTENT', 'REPORTS']]
    codata = [
        (1, 'Mineraltype', data.Mineraltype),
        (2, 'Separation_Method', data.Separation_Method),
        (3, 'Reagent_Used', data.Reagent_Used),
        (4, 'Reagent_Concentration', data.Reagent_Concentration + ' %'),
        (5, 'Separation_Time', data.Separation_Time + ' minutes'),
        (6, 'Energy_Consumption', data.Energy_Consumption  + ' kwh'),
        (7, 'min_efficiency', data.min_efficiency + ' %'),

    ]
    for eng in codata:
        cotable.append(eng)

    table3 = Table(cotable)
    table3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightskyblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    table3_name = Paragraph("<b>MINERAL SEPARATION TEAM REPORT</b>", table_name_style)
    elements.append(table3_name)
    elements.append(table3)
    elements.append(Spacer(1, 95))

    # Table 4: Module 4 TEAM Report
    foamtable = [['S.No', 'CONTENT', 'DETAILS']]
    foamdata = [
        (1, 'Deacetylation Method', data.Deacetylation_Method ),
        (2, 'Reaction Temperature', data.Reaction_Temperature +' °C'),
        (3, 'Reaction Time', data.Reaction_Time + ' hours'),
        (4, 'Degree Deacetylation', data.Degree_Deacetylation + ' %'),
        (5, 'Ash Content', data.Ash_Content + ' %'),
        (6, 'Deacetyl Efficiency', data.deacetyl_efficiency + ' %'),
    ]
    for foam in foamdata:
        foamtable.append(foam)

    table4 = Table(foamtable)
    table4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightskyblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    table4_name = Paragraph("<b>DEACETYLATION REPORT</b>", table_name_style)
    elements.append(table4_name)
    elements.append(table4)
    elements.append(Spacer(1, 35))

    # Table 5: Module 5 TEAM Report
    puritytable = [['S.No', 'CONTENT', 'DETAILS']]
    qadata = [
        (1, 'chitosan_extract_method', data.chitosan_extract_method ),
        (2, 'chit_reagent', data.chit_reagent ),
        (3, 'viscosity', data.viscosity+' cP'),
        (4, 'chit_reagent_concentration', data.chit_reagent_concentration + ' %'),
        (5, 'chitosan_efficiency', data.chitosan_efficiency + ' %'),
    ]
    for qa in qadata:
        puritytable.append(qa)

    table5 = Table(puritytable)
    table5.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightskyblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    table5_name = Paragraph("<b>CHITOSAN REPORT</b>", table_name_style)
    elements.append(table5_name)
    elements.append(table5)
    elements.append(Spacer(1, 35))

    ### TIME
    table6_name = Paragraph("<b>PROCESSING TIME</b>", table_name_style)
    elements.append(table6_name)
    timetable = [['S.No', 'TIMETAKEN'],['1', data.process_time]]

    table6 = Table(timetable)
    table6.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightskyblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table6)
    elements.append(Spacer(1, 15))


    # Add the graph image to the PDF
    generate_graph_path = image_pdf(data, pname, pid)
    graph_image = Image(generate_graph_path, 6 * inch, 4 * inch)
    elements.append(graph_image)

    # Build the PDF
    doc.build(elements)

    # Get PDF content from the buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    # Read the PDF content
    reader = PdfReader(BytesIO(pdf_data))
    writer = PdfWriter()

    # Add the pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt the PDF
    writer.encrypt(password)

    # Save the PDF with password protection
    protected_buffer = BytesIO()
    writer.write(protected_buffer)
    protected_pdf_data = protected_buffer.getvalue()
    protected_buffer.close()

    # Define the path to save the PDF file
    pdf_path = os.path.join(BASE_DIR, 'Reports', filename)

    # Save the PDF file in the specified path
    with default_storage.open(pdf_path, 'wb') as pdf_file:
        pdf_file.write(protected_pdf_data)

    # Save the path in the report_path field of the Chitosan_Productions instance
    data.report_path = pdf_path
    data.save()

    return pdf_path


def chitosan_mng_approve(request, id):
    if 'administrator' in request.session:
        values = Chitosan_Productions.objects.get(id=id)
        values.chitosan_report_mng = True
        values.save()
        messages.success(request, "Chitosan Team Reports are approved and Final Report Generated.")

        pdf_path = generate_pdf(id)
        print('PDF saved at:', pdf_path)

        return redirect("/manager/chitosan_report_page/")
    else:
        return redirect("/manager/chitosan_report_page/")





def chitosan_mng_reject(request,id):
    if 'administrator' in request.session:
        values = Chitosan_Productions.objects.get(id=id)
        values.delete()
        messages.success(request, "Chitosan Team Reports are rejected by Manager")
        return redirect("/manager/chitosan_report_page/")
    else:
        return redirect("/manager/chitosan_report_page/")


# ##################################################
# ############################################################
# #################### FINAL REPORT VIEW #####################
#

def final_report_page(request):
    datas = Chitosan_Productions.objects.filter(chitosan_report_mng=True)
    return render(request, '05_Manager/17_Final_Report.html', {'datas': datas})



from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from Manager.models import *

import os

def view_final_report(request, id):
    data = get_object_or_404(Chitosan_Productions, id=id)
    if not data.report_path:
        raise Http404("Report not found.")
    pdf_path = data.report_path
    if not os.path.exists(pdf_path):
        raise Http404("File does not exist.")
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')








