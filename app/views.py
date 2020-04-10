from django.shortcuts import render
from django.http import HttpResponse
import datetime,requests

#SMS FUNCTION
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        'apikey': apiKey,
        'secret': secretKey,
        'usetype': useType,
        'phone': phoneNo,
        'message': textMessage,
        'senderid': senderId
    }
    return requests.post(reqUrl, req_params)



# Create your views here.


def home(request):
    time=str(datetime.datetime.now())
    return render(request, 'home.html', {'time':time.upper()})


def sms(request):
    phone=str(request.POST['phone'])
    msg=request.POST['msg']
    URL = 'https://www.way2sms.com/api/v1/sendCampaign'
    response = sendPostRequest(URL, 'YNL842CKDC4MHPV1JFHUNX6Y7TFTKXTZ', '2I6AP4SGPDIIIPZP', 'stage', phone, 'waysms', msg)
    return HttpResponse("sent successfully")

