from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from Chitosan_Synthesis.models import *
from Manager.models import *
import pandas as pd
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

def chitosan_home_page(request):
    return render(request,'04_Chitosan/02_home_page.html')


def chitosan_register(request):
    if request.method == 'POST':
        username = request.POST['username'].title()
        email    = request.POST['email']
        contact  = request.POST['contact']
        password = request.POST['password']

        try:
            existing_user = Chitosan_teams.objects.get(email=email)
            messages.error(request, 'Email already taken. Try another!')
            return redirect('/chitosan_synthesis/chitosan_register/')

        except Chitosan_teams.DoesNotExist:
            try:
                new_team = Chitosan_teams(username=username, email=email, contact=contact, password=password)
                new_team.save()
                messages.success(request, 'Successfully chitosan Synthesis Team Registered')
                return render(request, '04_Chitosan/01_login_page.html')

            except IntegrityError as e:
                messages.error(request,f'An error occurred while registering: {e}')
                return redirect('/chitosan_synthesis/chitosan_register/')
    return render(request, '04_Chitosan/01_login_page.html')


def chitosan_login(request):
    if request.method=='POST':
        uemail = request.POST['useremail']
        upassword = request.POST['password']
        try:
            user = Chitosan_teams.objects.get(email=uemail)
            if user.password == upassword:
                if user.chitosan_login_approve:
                    request.session['chitosan'] = uemail
                    messages.success(request, 'Chitosan Team  Successfully Logged In')
                    return redirect('/chitosan_synthesis/chitosan_home/')
                else:
                    messages.success(request, 'Please Wait for Admin Approval')
                    return redirect('/chitosan_synthesis/chitosan_login/')
            else:
                messages.error(request, 'Incorrect password. Please try again')
                return redirect('/chitosan_synthesis/chitosan_login/')

        except ObjectDoesNotExist:
            messages.error(request, 'No Chitosan Synthesis Team with these credentials.')
            return redirect('/chitosan_synthesis/chitosan_login/')
    return render(request, '04_Chitosan/01_login_page.html')


def chitosan_logout(request):
    try:
        if 'chitosan' in request.session:
            print('Chitosan Login:',request.session['chitosan'])
            del request.session['chitosan']
            messages.success(request, 'Chitosan Synthesis Team  logged out successfully')
    except KeyError:
        messages.error(request, 'Error occurred during logout')
    return redirect('/')



#################################### START PROCESS
#########################################


def deacetyl_chitosan_viewdata(request):
    datas = Chitosan_Productions.objects.filter(deacetyl_report_mng=True)
    return render(request,'04_Chitosan/03_Deacetylation_Report.html',{'datas':datas})


def deacetyl_chitosan_detailedview(request,id):
    details = Chitosan_Productions.objects.get(id=id)
    return render(request, '04_Chitosan/04_Deacetylation_Deatiled_View.html', {'details': details})


#### Method Adoption Page

def chitosan_method_page(request):
    datas = Chitosan_Productions.objects.filter(deacetyl_report_mng=True)
    return render(request,'04_Chitosan/05_Method_Adoption.html',{'datas':datas})



def chitosan_method_selection_page(request, id):
    print('Ready to Upload ...')
    try:
        details = Chitosan_Productions.objects.get(id=id)
    except Chitosan_Productions.DoesNotExist:
        messages.error(request, 'Chitosan Production not found.')
        return redirect('/chitosan_synthesis/chitosan_method_page/')

    if request.method == "POST":
        chit_extract_method   = request.POST.get('chitin_extraction_method')
        chit_reagent          = request.POST.get('chitosan_synthesis_reagent')
        viscosity             = request.POST.get('viscosity')
        chit_reagent_concentration  = request.POST.get('reagent_concentration')

        try:
            print(chit_extract_method)
            details.chitosan_extract_method = chit_extract_method
            details.chit_reagent        = chit_reagent
            details.viscosity           = viscosity
            details.chit_reagent_concentration = chit_reagent_concentration
            details.chitosan_method = True
            details.save()
            messages.success(request, 'Chitosan Methods are Adopted Successfully')
            return redirect('/chitosan_synthesis/chitosan_method_page/')
        except Exception as e:
            messages.error(request, f'Error in Updating New Entries: {str(e)}')
            return redirect('/chitosan_synthesis/chitosan_method_page/')

    return render(request, '04_Chitosan/06_Method_Selction_Page.html', {'details': details})


#### CHITOSAN START PROCESS

def chitosan_start_process_page(request):
    datas = Chitosan_Productions.objects.filter(chitosan_method=True)
    return render(request, '04_Chitosan/07_Chitosan_Process.html', {'datas': datas})









from sklearn.svm import SVR

def chitosan_start_analyse(request, id):
    import os
    import time
    import pandas as pd
    from pathlib import Path
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from sklearn.preprocessing import StandardScaler

    detail = Chitosan_Productions.objects.get(id=id)

    # Start timer for performance measurement
    start_time = time.time()

    # Define the path to the dataset
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = os.path.join(BASE_DIR, 'Utility/04_Chitosan.csv')

    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        messages.error(request, "Dataset not found.")
        return redirect('/chitosan_synthesis/chitosan_start_process_page/')
    except pd.errors.EmptyDataError:
        messages.error(request, "Dataset is empty.")
        return redirect('/chitosan_synthesis/chitosan_start_process_page/')
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('/chitosan_synthesis/chitosan_start_process_page/')

    # Define features and labels
    features = df[['Viscosity (cP)', 'Reagent Concentration (%)', 'Required Purity (%)',
                   'Desired Quantity (kg)']]
    labels = df[['Chitosan Synthesis Efficiency (%)']]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the Support Vector Regressor model
    svr_model = SVR(kernel='rbf')
    svr_model.fit(X_train_scaled, y_train.values.ravel())

    # Make predictions on the test set
    predictions = svr_model.predict(X_test_scaled)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Prepare user input for prediction
    user_input = {
        'Viscosity (cP)'           : detail.viscosity,
        'Reagent Concentration (%)': detail.chit_reagent_concentration,
        'Required Purity (%)'       : detail.purity,
        'Desired Quantity (kg)'     : detail.quantity,
    }

    user_df = pd.DataFrame([user_input])
    user_scaled = scaler.transform(user_df)

    # Make predictions for the user input
    user_predictions = svr_model.predict(user_scaled)
    chitosan_efficiency = user_predictions[0]
    chitosan_efficiency = round(chitosan_efficiency, 2)

    # Print predictions for debugging
    print(f'chitosan_efficiency: {chitosan_efficiency}')

    # Record completion time for performance measurement
    end_time = time.time()
    analyse_time = '{} seconds'.format(round(end_time - start_time, 3))

    print('Analysed time', analyse_time)

    # Save the results
    detail.process_time = analyse_time
    detail.chitosan_efficiency = chitosan_efficiency
    detail.chitosan_report = True
    detail.save()

    # Display success message and redirect
    messages.success(request, "Chitosan Process Done")
    return redirect('/chitosan_synthesis/chitosan_start_process_page/')





def chitosan_report_page(request):
    datas = Chitosan_Productions.objects.filter(chitosan_report=True)
    return render(request, '04_Chitosan/08_Chitosan_Report_Page.html', {'datas': datas})


def chitosan_report_view(request,id):
    detail = Chitosan_Productions.objects.get(id=id)
    return render(request, '04_Chitosan/09_Chitosan_Detailed_Report.html', {'detail': detail})

####################################################################################
####################### BLOCK CHAIN ENCRYPTION DONE ###########################

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



def generate_encryption_key():
    return base64.urlsafe_b64encode(Fernet.generate_key()).decode('utf-8')

def encrypt_data(report_detail, key):
    fernet = Fernet(key)
    encrypted_data = {}
    for field, value in report_detail.items():
        encrypted_value = fernet.encrypt(str(value).encode()).decode('utf-8')
        encrypted_data[field] = encrypted_value
    return encrypted_data


def chitosan_report_encryption(request, id):
    data = Chitosan_Productions.objects.get(id=id)
    report_detail = {
        'chitosan_extract_method': data.chitosan_extract_method,
        'chit_reagent': data.chit_reagent,
        'viscosity': data.viscosity,
        'chit_reagent_concentration': data.chit_reagent_concentration,
        'chitosan_efficiency': data.chitosan_efficiency,
    }

    # Generate encryption key
    report_key = generate_encryption_key()
    key_bytes = base64.urlsafe_b64decode(report_key.encode('utf-8'))

    # Encrypt the report details
    encrypted_report = encrypt_data(report_detail, key_bytes)

    # Create blockchain and add encrypted data as a transaction
    blockchain = Blockchain()
    proof = blockchain.proof_of_work(blockchain.last_block.proof)
    block = blockchain.new_block(encrypted_report, proof)
    blockchain.add_block(block)

    # Save the encrypted data and block hash in the database
    data.encryption_key = report_key
    data.chitosan_encrypt = True
    for field, encrypted_value in encrypted_report.items():
        setattr(data, f"encrypted_{field}", encrypted_value)

    data.block_hash = block.hash  # Save the block hash in the database
    data.save()

    messages.success(request, "Data Successfully Encrypted and Added to Blockchain")
    messages.success(request, f"New Key Generated {report_key}")
    return redirect('/chitosan_synthesis/chitosan_report_page/')



### Send Email
def send_encrypt_key(request, id):
    try:
        data   = Chitosan_Productions.objects.get(id=id)
        pname  = data.name
        pid    = '100' + str(data.id)
        pdf_password = pname + pid
        encrypted_key = data.encryption_key

        email = 'demosample47@gmail.com'
        subject = 'Your Encrypted Key and PDF Password'
        message = f"""
        Dear Manager,

        Here are the details for the Chiosan Synthesis report:

        Name: {pname}
        ID: {pid}

        Encrypted Key: {encrypted_key}
        PDF Password: {pdf_password}

        Please use the above key and password to access the encrypted data.

        """
        send_mail(subject, message, 'demo@gmail', [email])
        data.key_sent = True
        data.save()
        messages.success(request, 'Key shared with the manager')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')

    return redirect('/chitosan_synthesis/chitosan_report_page/')

