from django.shortcuts import render
# import africastalking
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#creating 

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'firstname': user.first_name,


        })


#initialise SDK
username = "kagajugrace@gmail.com"
# api_key ="3e8c880168438d404cd6b56243959f9af4071030e892d15b14c513473d3e8e54"
# africastalking.initialize(username, api_key)


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

def registration(request):
    # select = Registration.objects.all().filter(telephone='0785528585').order_by('-id') 
    select = Registration.objects.all().order_by('-id')     #LIFO
    # select = Registration.objects.all()    
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        telephone = request.POST['telephone']
        insert = Registration(firstname=firstname,lastname=lastname,telephone=telephone)
        try:
            insert.save()
            return render(request,'registration.html',{'message':'have been successful','data':select})
        except:
            return render(request,'registration.html',{'message':'have failed','data':select})
    return render(request,'registration.html',{'data':select})  

def delreg(request,id):
    select = Registration.objects.all().order_by('-id')
    deleteInfos= Registration.objects.get(id=id).delete()
    return render(request,'registration.html',{'delmsg':'data has been deleted','data':select}) 
def updatereg(request,id):
    select = Registration.objects.all().order_by('-id')
    update= Registration.objects.get(id=id)
    if request.method=='POST':
        update.firstname= request.POST['firstname']
        update.lastname= request.POST['lastname']
        update.telephone= request.POST['telephone']
        try:
            update.save()
            return render(request,'updateregistration.html',{'message':'data has been updated','data':select,'update':update})
        except:
            return render(request,'updateregistration.html',{'message':'have failed','data':select,'update':update})
    return render(request,'updateregistration.html',{'data':select,'update':update}) 



# # =============== Building our endpoint ==========  

@csrf_exempt
def registerEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg= Registration.objects.all()
        serializer = RegisterSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)  #request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)


#delete/put/get  single data

# =======================Delete/put/get single data =====
@csrf_exempt
def deleteEndpoint(request,id):

    if request.method == 'GET':
        reg = Registration.objects.get(id=id)
        serializer = RegisterSerializer(reg, many=False)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        delete=Registration.objects.get(id=id).delete()
        return JsonResponse({'message':'Data has been deleted'},status=409)


    elif request.method == 'PUT':
        data = JSONParser().parse(request) 
        reg = Registration.objects.get(id=id)
        #/request.data
        serializer = RegisterSerializer(reg,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successfull updated','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def accountcreation(request):
   
    if request.method == 'GET':
        reg = User.objects.all().select_related('profile')
        serializer = UserSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Account created successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)

        
   




           
    
    
         





                

        