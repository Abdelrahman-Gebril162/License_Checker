from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import License
# Create your views here.

@api_view(["POST"])
def verify(request):
    try:
        license = request.data.get("license")
        mac = request.data.get("mac")
        program  = request.data.get("program")
    except:
        return JsonResponse({"result":False,"message":"add your id first to verify you"})
    client_license = License.objects.filter(id = license)
    if client_license.exists() and client_license.first().is_active == True and client_license.first().client_mac_id == mac and client_license.first().program.title == program:
        client = client_license.first()
        client.running_time += 1
        client.save()
        return JsonResponse({"result":True,"message":"you can work on scrip normally"})
    elif client_license.exists() and not client_license.first().is_active:
        return JsonResponse({"result":False,"message":"Ask admin to activate your license key"})
    elif not client_license.exists():
        return JsonResponse({"result":False,"message":"Invalid license key or use from different device ,Ask admin to add you to program"})

@api_view(["POST"])
def activate(request):
    #send mac id from user devicee na license key
    try:
        mac_address = request.data.get("mac")
        license = request.data.get("license")
        program  = request.data.get("program")
    except:
        return JsonResponse({"result":False,"mesage":"mac error"})
    client_license = License.objects.filter(id = license)

    if client_license.exists():
        if client_license.first().client_mac_id !="Null":
            return JsonResponse({"result":False,"mesage":"you already use this license"})
        elif client_license.first().program.title == program:
            client = client_license.first()
            client.is_active= True
            client.client_mac_id = mac_address
            client.save()
            return JsonResponse({"result":True,"message":"your account activated"})
    elif not client_license.exists():
        return JsonResponse({"result":False,"message":"You enter invalid license key!!"})

