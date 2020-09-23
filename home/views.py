from django.shortcuts import render
import africastalking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#initialise SDK
username = "kagajugrace@gmail.com"
api_key ="3e8c880168438d404cd6b56243959f9af4071030e892d15b14c513473d3e8e54"
africastalking.initialize(username, api_key)


# Create your views here.
def welcome (request):
    return render(request,'index.html')

def about (request):
    return render(request,'about.html')
@csrf_exempt

def ussdapp (request):
    if request.method == 'POST':
        #mandatory
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        num = text [:3]


        if text == '':
            response = 'CON welcome to MOMO \n'
            response += '1. Kohereza amafaranga \n'
            response += '2. Kugura'
        elif text == '1':
            response = 'CON Level:'+str (len(level))+' \n'
            response += '1. uri muri MOMO \n'
            response += '2. Ohereza mu mahanga'
        elif text == '1*1':
            response = 'CON Level:'+str (len(level))+' \n'
            response = 'CON nimero ya Mobile(Format 078xxxxxxx)' 
        elif num == '1*1' and int (len(level))==3 and str(level[2]) in str(level):
            response = "CON umubare w'amfaranga \n"
        elif num == '1*1' and int (len(level))==4 and str(level[3]) in str(level):
            response = "CON Enter PIN \n"
        elif num == '1*1' and int (len(level))==5 and str(level[4]) in str(level): 
            response = 'END Money sent' 


        else:
            response = 'END Invalid choice'


        return HttpResponse(response)
    return HttpResponse('Welcome')         




@csrf_exempt

def ussdmobi (request):
    if request.method == 'POST':
        #mandatory
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        level = text.split('*')
        response = ''
        num = text [:3]


        if text == '':
            response = 'CON welcome to MOMO \n'
            response += '1. Kohereza amafaranga \n'
            response += '2. Kugura'
        elif text == '1':
            response = 'CON Level:'+str (len(level))+' \n'
            response += '1. uri muri MOMO \n'
            response += '2. Ohereza mu mahanga'
        elif text == '1*1':
            response = 'CON Level:'+str (len(level))+' \n'
            response = 'CON nimero ya Mobile(Format 078xxxxxxx)' 
        elif num == '1*1' and int (len(level))==3 and str(level[2]) in str(level):
            response = "CON umubare w'amfaranga \n"
        elif num == '1*1' and int (len(level))==4 and str(level[3]) in str(level):
            response = "CON Enter PIN \n"
        elif num == '1*1' and int (len(level))==5 and str(level[4]) in str(level): 
            response = 'END Amafaranga yagiye' 


        else:
            response = 'END Invalid choice'


        return HttpResponse(response)
    return HttpResponse('Welcome')         





                

        