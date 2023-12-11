import json

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#----------------------------------------------------
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render

from requestforms.models import Transaction, User


def home(request):
    if request.method == "POST":
        username = request.POST['username']  
        password = request.POST['password']  
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.success(request,"Incorrect login, please try again")
            return redirect('home')
    else:
        return render(request, "home.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('home')


def transactions(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    #GET request
    if is_ajax:
        if request.method == 'GET':
            bloodFormRequests = list(Transaction.objects.select_related('User').values('User__Fullname','User__Occupation', 'User__Extension','System_Number','Pregnant','Recent_Transfusion','Diagnosis','High_Risk','GS','DAT','Other_Test','DateTimeRequired','Urgent','CMV','IR','RC','RC_Measurement','RC_Quantity','Platelets','Platelets_Measurement','Platelets_Quantity','FFP','FFP_Measurement','FFP_Quantity','Cryo','Cryo_Measurement','Cryo_Quantity'))
            return JsonResponse({'context': bloodFormRequests})
    
    #POST request
        if request.method == 'POST':
            
            data = json.load(request)

            #Get JSON data from POST request            
            json_objects = data.get('bloodRequestData')

            #Create database object using JSON objects
            Transaction.objects.create(DateTimeRequired=json_objects['DateTimeRequired'], Cryo=json_objects['CRYO'], Cryo_Measurement=json_objects['CRYO_Metric'], Cryo_Quantity=json_objects['CRYO_Quantity'], FFP=json_objects['FFP'], FFP_Measurement=json_objects['FFP_Metric'], FFP_Quantity=json_objects['FFP_Quantity'], Platelets=json_objects['PLT'], Platelets_Measurement=json_objects['PLT_Metric'], Platelets_Quantity=json_objects['PLT_Quantity'],RC=json_objects['RC'], RC_Measurement=json_objects['RC_Metric'], RC_Quantity=json_objects['RC_Quantity'], IR=json_objects['IR'], CMV=json_objects['CMV'], Other_Test=json_objects['OtherTest'], GS=json_objects['GS'], DAT=json_objects['DAT'], High_Risk=json_objects['HighRisk'], Pregnant=json_objects['Pregnant'], Recent_Transfusion=json_objects['Transfusion'], Diagnosis=json_objects['Diagnosis'], Urgent=json_objects['Urgent'], User=User.objects.get(User=request.user), System_Number=json_objects['SystemNumber'])
            
            #Return json response
            return JsonResponse({'status': 'Blood form submitted'})
        
        
        return JsonResponse({'status': 'Invalid request'}, status=400)
    
    else:
    
        return HttpResponseBadRequest('Invalid request')
