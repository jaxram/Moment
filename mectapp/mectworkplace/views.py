from.models import userid,bio,group,followers_group,posts,privatepost,like,privatereply,comment,followers_people,darkmode,notificationcount,ntime,logout,td,studentdetails,certificate_details,Events,EventUpdate,Registration,EventQueries,fcmdata
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from passlib.hash import pbkdf2_sha256
from django.http import JsonResponse
import json
import datetime
from django.core import serializers
import base64
import string
import random
import django
import pandas as pd
import pdfkit
import os
from pyfcm import FCMNotification
from django.conf import settings
import math
from django.db.models import Q,CharField
from django.db.models.functions import Lower
CharField.register_lookup(Lower, "lower")
global apikey

"""
To-Do-check :
    file null check
    check fn
"""
apikey="AAAA-_B-JEI:APA91bHIsUpMt9CwN0ZizYpX9k5-RzTY4_RbwI4pGkTJQelP738X7kCb0-_a8I5Sc84fKLbW9MF0qlRH4mgV7raSwHWDG8wQNsvmce7vt7IwueFIOnwRR8lbmUV9vtuzJisobkHPJZwM"
push_service = FCMNotification(apikey)
def check(useid,token):# user verification function
    """u5=UserId.objects.filter(userid=useid).values()
    for data in u5.values():
        if(data['webtoken']==token or data['androidtoken']==token):
            return True
        else:
            return False"""
    return True
def topicsubscription(apikey,tokens,topicname):
    try:

        subscribed = push_service.subscribe_registration_ids_to_topic(tokens,topicname)
        return 1
    except Exception as e:
        print(e)
        return 0
def topicunsubscription(apikey,tokens,topicname):
    try:
        #push_service = FCMNotification(apikey)
        subscribed = push_service.unsubscribe_registration_ids_from_topic(tokens,topicname)
        return 1
    except:
        return 0


def download(request):
    return render(request,'download.html')




@csrf_exempt
def initial_data(request):#t1(signup function)
    global email
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    email=request.POST.get('email')
    password=request.POST.get('pwd')
    enc=pbkdf2_sha256.hash(str(password)) #hashing password
    a1=userid.objects.filter(email=email).values()
    if check(useid,token):
        try:
            a=userid(email=email,password=enc)
            a.save()
            finaldict1.update({'status':'success'})
            finaldict1.update({'message':'success'})
            finaldict1.update({'data':{}})
            return HttpResponse(json.dumps(finaldict1))

        except :
            print('ierror')
            finaldict1.update({'status':'failed'})
            finaldict1.update({'message':'email already exists'})
            finaldict1.update({'data':{}})
            return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))






def t2(request):
    a=request.GET.get('request1')
    if a=='1':
        data=email
        return HttpResponse(data)
    else:
        pass



@csrf_exempt
def t3(request):
    global id1
    global acctype,designation
    k=[]
    e1=request.POST.get('email')
    g=userid.objects.filter(email=e1).values()
    try:
        for i in g:
            id1=i['userid']
        request.session['userid']=id1
        d1=darkmode(userid=request.session['userid'],dark=0)
        d1.save()
        d2=notificationcount(userid=request.session['userid'],nocount=0)
        d2.save()
        d3=ntime(userid=request.session['userid'],ptime=0,etime=0)
        d3.save()
        d4=logout(userid=request.session['userid'],lflag=0)
        d4.save()
        name=request.POST.get('name')
        mobile=request.POST.get('mobilenumber')
        request.session['mobile']=mobile
        acctype=request.POST.get('typeofaccount')
        designation=request.POST.get('designation')
        a=[name,mobile,acctype,designation]
        request.session['name']=name
        b1=bio(userid=request.session['userid'],name=name,mobile=mobile,acctype=acctype,designation=designation)
        b1.save()

        return HttpResponse(json.dumps('Success'))
    except:
        print('mobile number already exists')
        return HttpResponse(json.dumps('mobile number already exists'))




@csrf_exempt
def t4(request):

    req2=request.POST.get('request2')
    a=request.POST.get('imgdata')
    userid_1=request.POST.get('userid')

    if(userid_1!='' and userid_1!=None):
        userid_1=int(userid_1)
        request.session['userid']=userid_1
    if req2=='1':
        if a==None:
            c='static/images/profile-user.png'
            b2=bio.objects.filter(userid=request.session['userid']).update(profilepic=c)

            return HttpResponse('sucess')
        else:
            b=a[a.find(",")+1:]
            image_64_decode = base64.b64decode(b)
            c=r'static/dp/'+str(request.session['userid'])+r'_dp.jpg'
            image_result = open(c, 'wb+') # create a writable image and write the decoding result
            image_result.write(image_64_decode)

            b2=bio.objects.filter(userid=request.session['userid']).update(profilepic=c)

            return HttpResponse('sucess')
    else:
        pass




@csrf_exempt
def t30(request):
    userid_1=request.POST.get('userid')

    if(userid_1!='' and userid_1!=None):
        userid_1=int(userid_1)
        request.session['userid']=userid_1
    name=request.POST.get('name')
    request.session['name']=name
    mobile=request.POST.get('mobilenumber')
    request.session['mobile']=mobile
    print(request.session['name'])
    print(request.session['mobile'])
    i1=request.POST.get('rollno')
    print(i1)
    i2=request.POST.get('regno')
    print(i2)
    i3=request.POST.get('religion')
    i4=request.POST.get('blood')
    i5=request.POST.get('dob')
    i6=request.POST.get('address')
    i7=request.POST.get('brother')
    i8=request.POST.get('sister')
    i9=request.POST.get('fname')
    i10=request.POST.get('fmob')
    i11=request.POST.get('fmail')
    i12=request.POST.get('foccu')
    i13=request.POST.get('fincome')
    i14=request.POST.get('mname')
    i15=request.POST.get('mmob')
    i16=request.POST.get('mmail')
    i17=request.POST.get('moccu')
    i18=request.POST.get('mincome')
    i19=request.POST.get('sslcname')
    i20=request.POST.get('sslcadd')
    i21=request.POST.get('sslcyr')
    i22=request.POST.get('sslcmarks')
    i23=request.POST.get('hscname')
    i24=request.POST.get('hscadd')
    i25=request.POST.get('hscyr')
    i26=request.POST.get('hscmarks')
    i27=request.POST.get('maths')
    i28=request.POST.get('physics')
    i29=request.POST.get('chemistry')
    i30=request.POST.get('cutoff')
    i31=request.POST.get('dipcgpa')
    i32=request.POST.get('dipname')
    i33=request.POST.get('overall')
    i34=request.POST.get('communityrank')
    i35=request.POST.get('disability')
    i36=request.POST.get('amount')
    i37=request.POST.get('loanamount')
    i38=request.POST.get('room')
    i39=request.POST.getlist('box[]')
    i40=request.POST.getlist('box1[]')
    i41=request.POST.getlist('box2[]')
    i42=request.POST.get('gender')
    i43=request.POST.get('degree')
    i44=request.POST.get('admission')
    i45=request.POST.get('community')
    i46=request.POST.get('foccudes')
    i47=request.POST.get('moccudes')
    i48=request.POST.get('schoolloc')
    i49=request.POST.get('schooltype')
    i50=request.POST.get('mediumstudy')
    i51=request.POST.get('aftersslc')
    i52=request.POST.get('hscschoollocation')
    i53=request.POST.get('hscschooltype')
    i54=request.POST.get('hscmediumstudy')
    i55=request.POST.get('fgraduate')
    i56=request.POST.get('physicalc')
    i57=request.POST.get('eloan')
    i58=request.POST.get('hostel')
    i59=request.POST.get('scholarship')
    i60=request.POST.get('dept')
    print(i39)
    print(i40)
    print(i41)
    print(i42)

    a60=studentdetails.objects.filter(userid=request.session['userid']).values()
    if(len(a60)==0):
        a1=studentdetails(userid=request.session['userid'])
        a1.save()
    else:
        pass
    if request.session['mobile']!='':
        try:
            b1=bio.objects.filter(userid=request.session['userid']).update(mobile=request.session['mobile'])
            print('in elif')
            return HttpResponse('success')
        except:
            print('mobile number already exists')
            return HttpResponse('mobile number already exists')
    else:
        pass
    if request.session['name']!='':
        b1=bio.objects.filter(userid=request.session['userid']).update(name=request.session['name'])
        b2=studentdetails.objects.filter(userid=request.session['userid']).update(name=request.session['name'])
        return HttpResponse('success')
    else:
         b1=bio.objects.filter(userid=request.session['userid']).values()
         for i in b1.values():
             b2=studentdetails.objects.filter(userid=request.session['userid']).update(name=i['name'])
    if(i1==''or i1==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(rollno=i1)
        print('saved')
    if(i2==''or i2==None ):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(regno=i2)
        print('saved')
    if(i3==''or i3==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(religion=i3)
        print('saved')
    if(i4==''or i4==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(blood=i4)
        print('saved')
    if(i5==''or i5==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(dob=i5)
        print('saved')
    if(i6==''or i6==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(address=i6)
        print('saved')
    if(i7==''or i7==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(brother=i7)
        print('saved')
    if(i8==''or i8==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(sister=i8)
        print('saved')
    if(i9==''or i9==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(father_name=i9)
        print('saved')
    if(i10==''or i10==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(father_mobile=i10)
        print('saved')
    if(i11==''or i11==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(father_mail=i11)
        print('saved')
    if(i12==''or i12==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(father_occupation=i12)
        print('saved')
    if(i13==''or i13==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(father_income=i13)
        print('saved')
    if(i14==''or i14==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(mother_name=i14)
        print('saved')
    if(i15==''or i15==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(mother_mobile=i15)
        print('saved')
    if(i16==''or i16==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(mother_mail=i16)
        print('saved')
    if(i17==''or i17==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(mother_occupation=i17)
        print('saved')
    if(i18==''or i18==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(mother_income=i18)
        print('saved')
    if(i19==''or i19==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(school_sslc=i19)
        print('saved')
    if(i20==''or i20==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(school_address_sslc=i20)
        print('saved')
    if(i21==''or i21==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(sslc_year=i21)
        print('saved')
    if(i22==''or i22==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(sslc_marks=i22)
        print('saved')
    if(i23==''or i23==None and i==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(school_hsc=i23)
        print('saved')
    if(i24==''or i24==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(school_address_hsc=i24)
        print('saved')
    if(i25==''or i25==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hsc_year=i25)
        print('saved')
    if(i26==''or i26==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hsc_marks=i26)
        print('saved')
    if(i27==''or i27==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(maths_mark=i27)
        print('saved')
    if(i28==''or i28==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(physics_mark=i28)
        print('saved')
    if(i29==''or i29==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(chemistry_mark=i29)
        print('saved')
    if(i30==''or i30==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(cutoff=i30)
        print('saved')
    if(i31==''or i31==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(diploma_cgpa=i31)
        print('saved')
    if(i32==''or i32==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(college_diploma=i32)
        print('saved')
    if(i33==''or i33==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(TNEA_overall=i33)
        print('saved')
    if(i34==''or i34==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(TNEA_community=i34)
        print('saved')
    if(i35==''or i35==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(Disability=i35)
        print('saved')
    if(i36==''or i36==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(scholarship_amount=i36)
        print('saved')
    if(i37==''or i37==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(education_loan=i37)
        print('saved')
    if(i38==''or i38==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hostel_room=i38)
        print('saved')
    if(i39==''or i39==None):
        pass
    else:
        b=''
        for i in i39:
           b=b+'__'+i
        print(b)
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(achievements=b)
        print('saved')
    if(i40==''or i40==None):
        pass
    else:
        b1=''
        for i in i40:
           b1=b1+'__'+i
        print(b1)
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(scholarship_details=b1)
        print('saved')
    if(i41==''or i41==None):
        pass
    else:
        b2=''
        for i in i41:
           b2=b2+'__'+i
        print(b2)
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(extra_curricular=b2)
        print('saved')
    if(i42==''or i42==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(gender_user=i42)
        print('saved')
    if(i43==''or i43==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(degree=i43)
        print('saved')
    if(i44==''or i44==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(degree_details=i44)
        print('saved')
    if(i45==''or i45==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(community=i45)
        print('saved')
    if(i46==''or i46==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(foccupation_type=i46)
        print('saved')
    if(i47==''or i47==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(moccupation_type=i47)
        print('saved')
    if(i48=='' or i48==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(school_location=i48)
        print('saved')
    if(i49==''or i49==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(school_type=i49)
        print('saved')
    if(i50==''or i50==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(mediumstudy=i50)
        print('saved')
    if(i51=='' or i51==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(sslcafter=i51)
        print('saved')
    if(i52==''or i52==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hscschoollocation=i52)
        print('saved')
    if(i53==''or i53==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hscschooltype=i53)
        print('saved')
    if(i54==''or i54==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hscmediumstudy=i54)
        print('saved')
    if(i55==''or i55==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(firstgraduate=i55)
        print('saved')
    if(i56==''or i56==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(physically_challenged=i56)
        print('saved')
    if(i57==''or i57==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(eloan=i57)
        print('saved')
    if(i58==''or i58==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(hostel=i58)
        print('saved')
    if(i59==''or i59==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(scholarship=i59)
        print('saved')

    if(i60==''or i60==None):
        pass
    else:
        a1=studentdetails.objects.filter(userid=request.session['userid']).update(dept=i60)
        print('saved')

    return HttpResponse('success')




def t31(request):
    tar=request.GET.get('target')
    if tar=='1':
        return HttpResponse(json.dumps(request.session['userid']))
    else:
        pass




def edit(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'editprofile.html',{'s':s})

@csrf_exempt
def editprofdetails(request):
    useid=int(request.headers['X-User'])
    token=request.headers['X-Token']

    name=request.POST.get('name')
    regnum=request.POST.get('regnum')
    email=request.POST.get('email')
    phone=request.POST.get('phone')

    ext=request.POST.get('extension')

    if(check(useid,token)):
        if(name!=None and name!=''):
            b1=bio.objects.filter(userid=useid).update(name=name)
        if(regnum!=None and regnum!=''):
            b1=bio.objects.filter(userid=useid).update(reg_no=regnum)
        if(email!=None and email!=''):
            b1=bio.objects.filter(userid=useid).update(altemail=email)
        if(phone!=None and phone!=''):
            b1=bio.objects.filter(userid=useid).update(mobile=phone)
        if(ext!=None and ext!=''):
            k=request.FILES['file']
            now=datetime.datetime.now()
            t=now.strftime("%d-%m-%y %H:%M:%S")
            bioobj=bio.objects.filter(userid=useid).values()
            for data in bioobj.values():
                urlsplit=data['profilepic'].split('/')
            if(urlsplit[2]!="profile-user.png"):
                path = os.path.join(f"/home/mectmoment/Moment/mectapp/static/dp/", urlsplit[2])
                os.remove(path)
                print("old dp deleted")
            c=r'static/dp/'+str(useid)+'_'+'dp_'+str(t)+'.'+str(ext)
            print(c)
            with open(f'/home/mectmoment/Moment/mectapp/{c}', 'wb+') as destination:
                for chunk in k.chunks():
                    destination.write(chunk)
                print("file saved successfully")
            b1=bio.objects.filter(userid=useid).update(profilepic=c)
            print('new dp updated')
        return HttpResponse(1)
    else:
        return HttpResponse(0)
@csrf_exempt
def init_app(request):
    req=request.POST.get('request')
    if(req=='1'):
        useid=request.headers['X-User']
        token=request.headers['X-Token']
        u5=userid.objects.filter(userid=useid).values()
        for data in u5.values():
            if(data['webtoken']==token or data['androidtoken']==token):
                return HttpResponse('1')
            else:
                return HttpResponse('0')
    else:
        return HttpResponse('0')
@csrf_exempt  #disable csrf verification for post request
def authenticate(request):#t5(Login verification function)
    login=request.POST.get('login')
    mail=request.POST.get('email')
    password=request.POST.get('password')
    platform=request.POST.get('isweb')
    fcm=request.POST.get('fcmtoken')
    apikey="AAAA-_B-JEI:APA91bGTzkC8n_fsX0NuoQY5p7xY4iDzhOXmmKuX1Fr6Mtwbnl3CZNPle-8S17Bs-v3leYrjMesUl4Xy8FdZVVsYkHQI5k-6Dspd1XtUVtfwiliNTiXQu4EuAAp6_bYK0BY6oCl0OLND"
    #print(platform)
    #print(type(platform))
    #data=[]
    fdata={}
    tokens=[]
    token=[]
    stafftoken=[]
    if(login=='1'):
        g=userid.objects.all().values()
        for i in g.values():
            j=i['email']

            if j==mail:
                k=userid.objects.filter(email=mail).values()
                for j in k:
                    l=j['password']
                    id1=int(j['userid'])
                    request.session['userid']=id1

                    usertype=j['usertype']
                    enc=pbkdf2_sha256.verify(password,l)

                    if enc==True:
                        fcheck=fcmdata.objects.filter(userid=id1).values()
                        if(len(fcheck)==0):
                            now=datetime.datetime.now()
                            t=now.strftime("%d/%m/%y %H:%M:%S")
                            ftoken=fcmdata(userid=id1,fcmtoken=fcm,topics_subscribed="MECT-General",time_sub=t)
                            ftoken.save()
                            print("fcm token details saved")
                            tokens.append(fcm)
                            if(topicsubscription(apikey,tokens,"MECT-General")==1):
                                print(" MECT-General Topic subscribed")
                            else:
                                print("Error subscribing the MECT-General topic")

                        else:
                            now=datetime.datetime.now()
                            t=now.strftime("%d/%m/%y %H:%M:%S")
                            token.append(fcm)
                            if(topicsubscription(apikey,token,"MECT-General")==1):
                                print(" MECT-General Topic subscribed")
                            fcheck=fcmdata.objects.filter(userid=id1).update(fcmtoken=fcm,time_sub=t)
                            print("fcm details updated")
                        print('password true')
                        if(isstaff(id1)):
                            print('ull')
                            b1=bio.objects.filter(userid=id1).values()
                            for data in b1.values():
                                name=data["name"].split(" ")
                                name1=""
                                for d in name:
                                    name1=name1+d
                            stafftoken.append(fcm)

                            if(topicsubscription(apikey,stafftoken,"tutor_"+str(id1)+"_"+str(name1))==1):#tutor_id_name
                                print("tutor_",id1,name)
                                now=datetime.datetime.now()
                                t=now.strftime("%d/%m/%y %H:%M:%S")
                                ftoken=fcmdata(userid=id1,fcmtoken=fcm,topics_subscribed="tutor_"+str(id1)+"_"+str(name1),time_sub=t)
                                ftoken.save()
                        #print(res)
                        fdata.update({'Status':1})
                        #fdata.update({'token':res})
                        fdata.update({'userid':request.session['userid']})
                        v1=bio.objects.filter(userid=request.session['userid']).values()
                        for data in v1.values():
                            fdata.update({'username':data['name']})
                            fdata.update({'userdp':data['profilepic']})
                        v2=userid.objects.filter(userid=request.session['userid']).values()
                        for data in v2.values():
                            fdata.update({'useremail':data['email']})

                        fdata.update({'usertype':usertype})
                        #data.append(fdata)
                        #print(data)
                        response = JsonResponse(fdata)
                        print('88888888888888888888888888888')
                        if not request.session.session_key:
                            request.session.create()
                        print(request.session.session_key)
                        response.headers['X-Token'] = request.session.session_key
                        #print('...................')
                        #print(response.headers['X-Token'])
                        #print(response.items())
                        if(platform=='1'):
                            l11=userid.objects.filter(userid=request.session['userid']).update(webtoken=request.session.session_key)

                        elif(platform=='0'):
                            l11=userid.objects.filter(userid=request.session['userid']).update(androidtoken=request.session.session_key)
                        return response
                    else:
                        print('password incorrect')
                        fdata.update({'Status':2})
                        fdata.update({'userid':0})
                        fdata.update({'usertype':0})
                        return HttpResponse(json.dumps(fdata))
        else:
            fdata.update({'Status':0})
            fdata.update({'userid':0})
            fdata.update({'usertype':0})
            return HttpResponse(json.dumps(fdata))
    else:
        fdata.update({'Status':3})
        fdata.update({'userid':0})
        fdata.update({'usertype':0})
        return HttpResponse(json.dumps(fdata))



def index(request):
    try:
        l1=logout.objects.filter(userid=request.session['userid']).values()
        print(len(l1))
        if len(l1)==0:
            return render (request,'index.html')
        else:
            for i in l1.values():
                if i['lflag']==1:
                    return render (request,'index.html')
                else:
                    b7=darkmode.objects.filter(userid=request.session['userid'])
                    for i in b7.values():
                        del i['id']
                        del i['userid']
                    s=i['dark']
                    return render (request,'home.html',{'s':s})
    except:
        return render (request,'index.html')



def index1(request):
    return render (request,'index1.html')


@csrf_exempt
def t6(request):
    a=request.POST.get('groupimgdata')
    gpname=request.POST.get('groupname')
    create=request.POST.get('create_group')
    print(gpname)
    if create=='1':
        b=a[a.find(",")+1:]
        image_64_decode = base64.b64decode(b)
        c=r'static/group/'+r'group_'+str(request.session['userid'])+r'_dp.jpg'

        image_result = open(c, 'wb+') # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        b3=group(adminid=request.session['userid'],groupname=gpname,groupdp=c)
        b3.save()
        return HttpResponse('success')
    else:
        pass



@csrf_exempt
def search_list(request):#t7
    finaldict1={}
    name=request.GET.get('name').strip().lower()
    s1=bio.objects.filter(Q(name__lower__contains=name)).values()
    s2=group.objects.filter(Q(groupname__lower__contains=name)).values()
    s3=bio.objects.filter(Q(reg_no__lower__contains=name)).values()
    bd=[]
    gd=[]
    rd=[]
    l=[]
    for i in s1.values():
        del i['mobile']
        del i['acctype']
        del i['designation']
        i.update({'isUser':1})
        bd.append(i)


    for j in s2:
        del j['adminid']
        j.update({'isUser':0})
        gd.append(j)
    for i in s3:
        del i['mobile']
        del i['acctype']
        del i['designation']
        i.update({'isUser':1})
        rd.append(i)
    l=gd+bd+rd
    #print(l)
    finaldict1.update({'status':4})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':l})
    return HttpResponse(json.dumps(finaldict1))


@csrf_exempt
def t8(request):
    type1=request.POST.get('type1')
    searchid=request.POST.get('id')
    request.session['searchid']=searchid
    print(type1)
    return HttpResponse('success')

@csrf_exempt
def t9(request):
    type1=request.POST.get('type1')
    grid=request.POST.get('id')
    request.session['groupid']=grid
    print(type1)
    print(grid)
    return HttpResponse('success')



def prof(request,uid):
    print(uid)
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    print(s)
    return render(request,'profile.html',{'s':s})



def grp(request,gid):
    request.session['gid1']=gid
    print(request.session['gid1'])
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'groups.html',{'s':s})



def t22(request):
    v11=[]
    gp=request.GET.get('getprofile')
    searchid=request.GET.get('targetuserid')
    if(searchid!='' or searchid!=None):
        request.session['searchid']=searchid
    else:
        pass
    print(gp)
    app=[]
    fst=[]
    followers=[]
    a='fstatus:0'
    b='fstatus:1'
    b1=bio.objects.filter(userid=request.session['searchid']).values()
    for i in b1.values():
        del i['userid']

        del i['acctype']
        app.append(i)
    print(app)
    fp=followers_people.objects.filter(id_follow=request.session['userid']).filter(id_to_follow=request.session['searchid']).values()
    print(fp)
    if len(fp)==0:
        fst.append(a)
    else:
        for j in fp.values():
            if j['id_to_follow']!=request.session['searchid'] and j['id_follow']!=request.session['userid']:
                fst.append(a)
                print('checked')
            else:
                fst.append(b)
                print('gosh')
    print(fst)
    followers=app+fst
    return HttpResponse(json.dumps(followers))


@csrf_exempt
def t23(request):
    follow=request.POST.get('follow')
    if follow=='1':
        fp1=followers_people(id_follow=request.session['userid'],id_to_follow=request.session['searchid'])
        fp1.save()
        print('saved')
        return HttpResponse('success')
    else:
        fp2=followers_people.objects.filter(id_follow=request.session['userid']).filter(id_to_follow=request.session['searchid']).delete()
        return HttpResponse('deleted')



def pre_post(request):#t10
    pdata=request.GET.get('postdata')
    finaldict1={}
    d=[]
    f=[]
    g=[]
    if pdata=='1':
        a=bio.objects.filter(userid=request.session['userid']).values()
        for i in a.values():
            del i['mobile']
            del i['acctype']
            del i['designation']
            d.append(i)
            g=group.objects.all().values()
            for j in g.values():
                del j['groupid']
                del j['adminid']
                del j['groupdp']
                f.append(j)
        g=d+f
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':g})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'failed'})
        finaldict1.update({'message':'postadata variable not set'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))




@csrf_exempt
def add_post_data(request):#t11
    finaldict1={}
    li=[]
    useid=int(request.headers['X-User'])
    token=request.headers['X-Token']
    if(check(useid,token)):
        posttext1=request.POST.get('posttext')
        posttext=posttext1.encode('unicode-escape').decode('utf-8')
        visibility=request.POST.get('postprivacy')#0 -public 1-private
        print('addddddddddddddddddpost visibility',visibility)
        a=request.POST.get('isimg')
        request.session['useid']=useid
        groupid=request.POST.get('groupid')
        fileattach=request.POST.get('fileattached')
        selectedstaff=request.POST.get('selectedstaff')
        print('selectedstaff    post ',selectedstaff)
        n1=12
        res=''.join(random.choices(string.ascii_uppercase+string.digits,k=n1))

        if(fileattach=='1'):
            k=request.FILES['file']
            print('/////]]]')
            print(k)
            fname=request.POST.get('filename')
            ext=request.POST.get('extension')
            print('extension: ',ext)
            file_size=len(k.read())

        if posttext=='' and a==None:
            print('no')
            return HttpResponse(0)
        else:
            if fileattach=='0':
                c=None
                ext=None
                file_size=None

            else:
                now=datetime.datetime.now()
                t=now.strftime("%Y-%m-%d %H:%M:")
                dotindex = str(k.name).rfind(".")
                trimres=str(k.name)[0:dotindex]
                c=r'static/post/'+str(trimres)+'_post_'+str(t)+str(request.session['useid'])+'_'+str(res)+"."+str(ext)
                z=posts.objects.all().values()
                if len(z)==0:
                     with open(f'/home/mectmoment/Moment/mectapp/{c}', 'wb+') as destination:
                        for chunk in k.chunks():
                            destination.write(chunk)
                else:
                    for i in z.values():
                        del i['postid']
                        del i['userid']
                        del i['groupid']
                        del i['postdata']
                        del i['posttime']
                        li.append(i)
                    print(li)
                    for i in li:
                        if i['fileurl']==c:
                            res=''.join(random.choices(string.ascii_uppercase+string.digits,k=n1))
                            #c=r'static/post/post_'+str(t)+str(request.session['useid'])+'_'+str(res)+"."+str(ext)
                            dotindex = str(k.name).rfind(".")
                            trimres=str(k.name)[0:dotindex]
                            c=r'static/post/'+str(trimres)+'_post_'+str(t)+str(request.session['useid'])+'_'+str(res)+"."+str(ext)


                        else:
                             with open(f'/home/mectmoment/Moment/mectapp/{c}', 'wb+') as destination:
                                for chunk in k.chunks():
                                    destination.write(chunk)
            print(posttext)

            now=datetime.datetime.now()
            t=now.strftime("%d/%m/%y %H:%M:%S")
            print(t)
            k=group.objects.filter(groupid=groupid).values()
            print(k)
            for i in k.values():
                j=i['groupid']
                gname=i['groupname']
            #print(type(j))
            b2=posts(userid=request.session['useid'],groupid=j,postdata=posttext,fileurl=c,posttime=t,extension=ext,filesize=file_size)
            b2.save()
            print('saved in db')

            k1=posts.objects.filter(userid=request.session['useid']).values()
            for i in k1.values():
                p=i['postid']
                request.session['p']=p
                u=i['groupid']
                request.session['u']=u
            if(visibility=='1' and j==3 ):
                if(selectedstaff!='' and selectedstaff!=None):
                    uid=selectedstaff.split(',')
                    for i in uid:
                        b=privatepost(userid=int(i),postid=p)
                        b.save()

                        print('private data saved')
                    b1=privatepost(userid=useid,postid=p)
                    b1.save()


            elif(visibility=='0' and j==3):
                stud=[]
                utd=td.objects.filter(student=useid).values()
                if(len(utd)==0):
                    utd=utd=td.objects.filter(staff=useid).values()
                for data in utd.values():
                    tutorid1=data['staff']
                ud=td.objects.filter(staff=tutorid1).values()
                for data in ud.values():
                    stud.append(data['student'])
                print('/////////ssss////////',stud)
                for data in stud:
                    b1=privatepost(userid=data,postid=p)
                    b1.save()
                b2=privatepost(userid=tutorid1,postid=p)
                b2.save()
            elif(visibility=='1' and j==1):
                if(selectedstaff!='' and selectedstaff!=None):
                    uid=selectedstaff.split(',')
                    for i in uid:
                        b=privatepost(userid=int(i),postid=p)
                        b.save()

                        print('private data saved')
                    b1=privatepost(userid=useid,postid=p)
                    b1.save()
            print(j,'lllllllllllll',visibility)
            bi=bio.objects.filter(userid=request.session['useid']).values()
            for data in bi.values():
                usname=data["name"]
            if(j==1 and visibility=='0'):
                print(".....................>>>>>>>>>>>>>>>>>>in notify")
                notify("MECT-General","New post in "+str(gname),str(usname)+" has posted in "+str(gname))
            elif(j==1 and visibility=='1'):
                tokens=[]
                if(selectedstaff!='' and selectedstaff!=None):
                    uid=selectedstaff.split(',')
                    for i in uid:
                        fcmdet=fcmdata.objects.filter(userid=int(i)).values()
                        for data in fcmdet.values():
                            tokens.append(data['fcmtoken'])
                    notifybatch(tokens,"New post in "+str(gname),str(usname)+" has posted in "+str(gname))

            elif(j==3 and visibility=='0'):
                f1=fcmdata.objects.filter(userid=request.session['useid']).values()
                for data in f1.values():
                    if(data["topics_subscribed"]!='MECT-General'):
                        notify(data["topics_subscribed"],"New post in "+str(gname),str(usname)+" has posted in "+str(gname))
                        print("notify triggered")
            elif(j==3 and visibility=='1'):
                tokens=[]
                print("in 3,1")
                if(selectedstaff!='' and selectedstaff!=None):
                    uid=selectedstaff.split(',')
                    print(uid,'oooooooooo')
                    for i in uid:
                        fcmdet=fcmdata.objects.filter(userid=int(i)).values()
                        for data in fcmdet.values():
                            tokens.append(data['fcmtoken'])
                            break
                    notifybatch(tokens,"New post in "+str(gname),str(usname)+" has posted in "+str(gname))

            return HttpResponse(1)
    else:

        return HttpResponse(0)


@csrf_exempt
def post_member_list(request):#t12
    finaldict1={}
    y=[]
    z=[]
    z1=[]
    z2=[]
    userid_1=request.headers['X-User']
    token=request.headers['X-Token']
    postid=request.POST.get('postid')
    if(userid_1!='' and userid_1!=None):
        request.session['userid']=int(userid_1)
    if(postid!='' and postid!=None):
        request.session['p']=int(postid)

    if(check(userid_1,token)):
        l1=bio.objects.filter(userid=request.session['userid']).values()
        for l in l1.values():
            k2=bio.objects.filter(acctype=0).values()
            for k in k2.values():
                del k['mobile']
                del k['acctype']
                del k['designation']
                z.append(k)
            for i in z:
                if i['userid']==request.session['userid']:
                    del i['userid']
                    del i['name']
                    del i['profilepic']
                else:
                    z1.append(i)
            z2.append(request.session['p'])
            z3={
                'members':z1,
                'postid':z2
                }

        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':z3})
        return HttpResponse(json.dumps(finaldict1))

    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))



@csrf_exempt
def privatepost_save(request):#t13
    postid=request.POST.get('postid')
    uid=(request.POST.getlist('userid[]'))
    userid_1=request.POST.get('userid')
    if(userid_1!='' and userid_1!=None):
        uid=userid_1.split(',')
    print(postid)

    for i in uid:
        b=privatepost(userid=i,postid=postid)
        b.save()
    return HttpResponse('success')


def t14(request):
    j=[]
    groups=request.GET.get('groups')
    if groups=='1':
        g=group.objects.all().values()
        for i in g.values():
            del i['adminid']
            j.append(i)
        print(j)
        return HttpResponse(json.dumps(j))
    else:
        pass



def t15(request):
    final=''
    userrequest=request.GET.get('userrequest')
    if userrequest=='1':
        final1=final+str((request.session['userid']))+","
        staff=bio.objects.filter(userid=request.session['userid']).values()
        for i in staff.values():
            final2=final1+str(i['acctype'])
        return HttpResponse(json.dumps(final2))
    else:
        print("else")
        pass

def filenameextract(name):
    x = name.rfind(".")
    splitedstring=name[12:x]
    return splitedstring

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def extensionresave(fileurl):

    b2=posts.objects.filter(fileurl=fileurl).values()
    print('b2------------------------------------------------------:',b2)
    for data in b2.values():
        extindex=data['fileurl'].rfind('.')
        ext=data['fileurl'][extindex+1:]
        b3=posts.objects.filter(fileurl=fileurl).update(extension=ext)
        print("Extension resaved")
    return ext
def home_content(request):#t16

    useid=int(request.headers['X-User'])
    token=request.headers['X-Token']
    extensions={"ppt":"application/vnd.ms-powerpoint",
    "pptx":"application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "pps":"application/vnd.ms-powerpoint",
    "doc":"application/msword",
    "docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "xls":"application/vnd.ms-excel",
    "xlsx":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "csv":"application/vnd.ms-excel",
    "c":"text/plain",
    "conf":"text/plain",
    "cpp":"text/plain",
    "py":"text/plain",
    "h":"text/plain",
    "log":"text/plain",
    "prop":"text/plain",
    "rc":"text/plain",
    "sh":"text/plain",
    "txt":"text/plain",
    "xml":"text/plain",
    "rtf":"application/rtf",
    "bmp":"image/bmp",
    "gif":"image/gif",
    "jpeg":"image/jpeg",
    "jpg":"image/jpeg",
    "png":"image/png",
    "m3u":"audio/x-mpegurl",
    "m4a":"audio/mp4a-latm",
    "m4b":"audio/mp4a-latm",
    "m4p":"audio/mp4a-latm",
    "mp2":"audio/x-mpeg",
    "mp3":"audio/x-mpeg",
    "mpga":"audio/mpeg",
    "ogg":"audio/ogg",
    "rmvb":"audio/x-pn-realaudio",
    "wav":"audio/x-wav",
    "wma":"audio/x-ms-wma",
    "wmv":"audio/x-ms-wmv",
    "3gp":"video/3gpp",
    "avi":"video/x-msvideo",
    "m4u":"video/vnd.mpegurl",
    "m4v":"video/x-m4v",
    "mov":"video/x-m4v",
    "mp4":"video/mp4",
    "mpe":"video/mpeg",
    "mpeg":"video/mpeg",
    "mpg":"video/mpeg",
    "mpg4":"video/mp4",
    "asf":"video/x-ms-asf",
    "pdf":"application/pdf",
    "apk":"application/vnd.android.package-archive",
    "htm":"text/html",
    "html":"text/html",
    "class":"application/octet-stream",
    "exe":"application/octet-stream",
    "jar":"application/java-archive",
    "js":"application/x-javascript",
    "wps":"application/vnd.ms-works"}


    if(check(useid,token)):
        request.session['userid']=int(useid)
        finaldict1={}
        filedetails=[]
        filedict={}
        a1=[]
        a2=[]
        a3=[]
        x=[]
        y=[]
        m10=[]
        request.session['m10']=m10
        n=[]
        l=[]
        o=[]
        q=[]
        r=[]
        s=[]
        t=[]
        u=[]
        a10=[]
        request.session['a10']=a10
        b10=[]
        request.session['b10']=b10
        l10=[]
        l12=[]
        s1=[]
        s2=[]
        s3=[]
        m11=[]
        request.session['m11']=m11
        m12=[]
        staffdetails={}
        staffs=[]

        staff=bio.objects.filter(acctype=0).values()
        for data in staff.values():
            staffdetails.update({"userid":data['userid']})
            staffdetails.update({"name":data['name']})
            staffdetails.update({"profilepic":data['profilepic']})
            if(data['designation']==0):
                staffdetails.update({"designation":'Head of the Department'})
            elif(data['designation']==1):
                staffdetails.update({"designation":'Associate Professor'})
            elif(data['designation']==2):
                staffdetails.update({"designation":'Assistant Professor'})
            staffs.append(staffdetails)
            staffdetails={}

        p=posts.objects.all().values()
        p1=privatepost.objects.all().values()
        l2=like.objects.filter(userid=request.session['userid']).values()
        for j in l10:
            l11=j['postid']
            l12.append
        for i in p.values():
            if((i['extension']==None or i['extension']=='' or i['extension']=='NULL')and i["fileurl"]!=None and i["fileurl"]!='NULL'):
                    ex=extensionresave(i["fileurl"])
                    #print("ull-------======")
                    filedict.update({'filetype':ex})
                    #print("saved-------======")
            else:

                if(i['extension']=="png" or i['extension']=="jpeg" or i['extension']=="jpg" or i['extension']=="gif" or i['extension']=="jfif"):
                    filedict.update({'isimage':1})
                    filedict.update({"fileurl":i["fileurl"]})
                    filedict.update({"filename":filenameextract(i["fileurl"])})
                    if(i['filesize']==None or i['filesize']=='NULL'):
                        fsize=1159023
                    else:
                        fsize=convert_size(int(i['filesize']))
                    filedict.update({'filesize':fsize})
                    filedict.update({'filetype':i['extension']})
                    filedetails.append(filedict)
                    filedict={}
                else:

                    if(i["fileurl"]!=None and i['filesize']!=None and i['extension']!=None):
                        filedict.update({'isimage':0})
                        filedict.update({"fileurl":i["fileurl"]})
                        filedict.update({"filename":filenameextract(i["fileurl"])})
                        #print(int(i['filesize']))
                        fsize=convert_size(int(i['filesize']))
                        filedict.update({'filesize':fsize})
                        for key in extensions:
                            if(key==i['extension']):
                                filedict.update({'filetype':extensions[key]})
                        filedetails.append(filedict)
                        filedict={}

            del i['fileurl']
            del i['extension']
            del i['filesize']
            postdatadecoded=i['postdata'].encode('utf-8').decode('unicode-escape').encode('utf-16','surrogatepass').decode('utf-16')
            i.update({'postdata':postdatadecoded})
            i.update({'filedetails':filedetails})
            filedetails=[]
            i.update({'likestatus':0})
            i.update({'commentdata':[]})
            i.update({'commenttime':[]})
            i.update({'commentstatus':0})
            i.update({'commentedby':[]})
            i.update({'commentcount':0})
            i.update({'dp':[]})
            i.update({'delete':0})
            request.session['m10'].append(i)
        request.session['m10'].reverse()
        #print(p1)
        for i in p1.values():
            n.append(i)
        for i in request.session['m10']:
            l.append(i['postid'])
        print(l)
        for j in n:
            del j['id']
            o.append(j)
        #print(o)
        #print(request.session['m10'])
        xy=[]
        for m in l:
            for j in o:
                if j['postid']==m:
                   xy.append(j['userid'])
                else:
                    #print('postid diffErent')
                    pass
            print(xy)
            flag=None
            for k in xy:
                #print('iiiiiiiiiiiiii')
                #print(type(k),type(request.session['userid']))
                if request.session['userid']==k:
                    flag=1
                    #print('flag is set')
                else:
                    pass
            if flag!=1 and len(xy)>0:
                flag=0
                #print('not ok')
            else:
                flag=1
            if flag==1:
                print('ok')
            else:
                #print(m)
                #print('444444444444444444')
                #print(request.session['m10'])
                request.session['m10']=[i for i in request.session['m10'] if not (i['postid']==m)]
            xy.clear()

        for i in request.session['m10']:
            k=i['userid']
            l=i['groupid']
            b1=bio.objects.filter(userid=k).values()
            bioval={}
            for data in b1.values():
                if(data['reg_no']==None or data['reg_no']==''):
                   data['reg_no']=None
                if(data['altemail']==None or data['altemail']==''):
                   data['altemail']=None
                bioval.update({'userid':data['userid']})
                bioval.update({'name':data['name']})
                bioval.update({'mobile':data['mobile']})
                bioval.update({'reg_no':data['reg_no']})
                bioval.update({'acctype':data['acctype']})
                bioval.update({'designation':data['designation']})
                bioval.update({'profilepic':data['profilepic']})
                bioval.update({'altemail':data['altemail']})
            t.append(bioval)
            b2=group.objects.filter(groupid=l).values()
            u.append(b2)
        for i in t:
            #print('11111111111111111111111111111111111111111')
            print(i)
            del i['userid']
            del i['mobile']
            del i['acctype']
            del i['designation']
            request.session['a10'].append(i)
        for i in u:
            for j in i.values():

                del j['adminid']
                request.session['b10'].append(j)
        for i in l2.values():
            del i['id']
            del i['liketime']
            del i['userid']
            l10.append(i)
        for i in l10:
            for j in request.session['m10']:
                if i['postid']==j['postid']:
                    j.update({'likestatus':1})
                    s1.append(j)
        request.session['m11']=request.session['m10'].copy()
        upcomment=[]
        f=comment.objects.all().values()
        for i in f.values():
            i.update({'dp':'NaN--:)'})
            a1.append(i)
        for j in request.session['m11']:
            for i in a1:
                if i['postid']==j['postid']:
                    #print('ppppppppppstid',i['postid'])
                    b1=bio.objects.filter(userid=i['userid']).values()
                    #print('b1111111111111111111',b1)
                    for k in b1.values():
                        i.update({'dp':k['profilepic']})
                        i.update({'commentedby':k['name']})
                        del i['id']
                        del i['userid']
                    upcomment.append(i)
                else:
                    pass

        j1=sorted(upcomment,key=lambda i: (i['postid'],i['commenttime']),reverse=True)
        commentdata = {}
        commenttime = {}
        dp={}
        commentedby={}
        postid_list=[]
        for i in j1:
            if i['postid'] not in postid_list:
                postid_list.append(i['postid'])
        #print('j1111111111111111111',j1)
        #print('ppppppppppppppppooooooooooooooddddddddddd',postid_list)
        for j in postid_list:
            commentdata[j] = [i['commentdata']  for i in j1 if i['postid'] == j]
            commenttime[j] =[i['commenttime']  for i in j1 if i['postid'] == j]
            commentedby[j]=[i['commentedby']  for i in j1 if i['postid'] == j]
            dp[j] =[i['dp']  for i in j1 if i['postid'] == j]
        updated_j1 = []
        #print('cooooooooooooooooooooooooooommmmmmmmeeeeeeeeeeeeeent',commentedby)
        for j in postid_list:
            temp_dict = {}
            temp_dict['postid'] = j
            temp_dict['commentdata'] = commentdata[j]
            temp_dict['commenttime'] = commenttime[j]
            temp_dict['dp'] = dp[j]
            temp_dict['commentedby']=commentedby[j]
            updated_j1.append(temp_dict)

        for i in updated_j1:
            for j in request.session['m10']:
                if i['postid']==j['postid']:
                    j.update({'commentdata':i['commentdata']})
                    j.update({'commenttime':i['commenttime']})
                    j.update({'dp':i['dp']})
                    j.update({'commentedby':i['commentedby']})

                    a3.append(j)

        #print(updated_j1)
        request.session['m11']=request.session['m10'].copy()
        request.session['final']=request.session['m10'].copy()
        #print('count----------')
        #print(request.session['m11'])
        z1=len(request.session['m11'])

        postcount=0
        for i in request.session['m11']:

            print((request.session['m11'][postcount]['commentdata']))
            if(len((request.session['m11'][postcount]['commentdata']))==0):
                i.update({'commentcount':0})
                postcount=postcount+1
            else:
                i.update({'commentcount':len(request.session['m11'][postcount]['commentdata'])})
                postcount=postcount+1
        for i in request.session['m11']:
            if i['userid']==request.session['userid']:
                i['delete']=1
            else:
                pass
        #print(z1)
        for i in request.session['m11'][0:10]:
            s.append(i)
        for i in request.session['a10'][0:10]:
            x.append(i)
        for i in request.session['b10'][0:10]:
            y.append(i)
        n11=bio.objects.filter(userid=request.session['userid']).values()
        for i in n11.values():
            request.session['n12']=i['profilepic']
            request.session['n13']=i['name']
        grpdetails=[]
        gpdet=[]
        g=group.objects.all().values()
        g1=group.objects.filter(groupid=1).values()
        for j in g.values():
            del j['adminid']
            grpdetails.append(j)
        for j in g1.values():
            del j['adminid']
            gpdet.append(j)
        tutordetails={}
        tutdet=td.objects.filter(student=request.session['userid']).values()

        if(len(tutdet)==0 and isstaff(request.session['userid'])==0):
            context={
                'post':s,
                'user':x,
                'postgroup':y,
                'userdp':request.session['n12'],
                'username':request.session['n13'],
                'staffdetails':staffs,
                'group':gpdet,
                'tutor':None,
                'length':z1
            }

        else:
            tutval={}
            wardlist=[]
            ward={}
            for data in tutdet.values():
                tutbio=bio.objects.filter(userid=data['staff']).values()
                for data in tutbio.values():
                    if(data['reg_no']==None or data['reg_no']==''):
                        data['reg_no']=None
                    if(data['altemail']==None or data['altemail']==''):
                        data['altemail']=None
                    tutval.update({'userid':data['userid']})
                    tutid=data['userid']
                    tutval.update({'name':data['name']})
                    #tutval.update({'mobile':data['mobile']})                                                                                                         bioval.update({'userid':data['userid']})
                    tutval.update({'reg_no':data['reg_no']})
                    tutval.update({'acctype':data['acctype']})
                    tutval.update({'profilepic':data['profilepic']})
                    tutval.update({'altemail':data['altemail']})
                    if(data['designation']==0):
                        tutval.update({"designation":'Head of the Department'})
                    elif(data['designation']==1):
                         tutval.update({"designation":'Associate Professor'})
                    elif(data['designation']==2):
                         tutval.update({"designation":'Assistant Professor'})

            if(len(tutval)==0 ):
                c1=td.objects.filter(staff=useid).values()
                for data in c1.values():
                    studid=data['student']
                    b1=bio.objects.filter(userid=studid).values()
                    for data1 in b1.values():
                        ward.update({'userid':data1['userid']})
                        ward.update({'name':data1['name']})
                        ward.update({'profilepic':data1['profilepic']})
                        wardlist.append(ward)
                        ward={}
            context={
                'post':s,
                'user':x,
                'postgroup':y,
                'userdp':request.session['n12'],
                'username':request.session['n13'],
                'staffdetails':staffs,
                'group':grpdetails,
                'tutor':tutval,
                'warddetails':wardlist,
                'length':z1
            }
        finaldict1.update({'status':1})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':context})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':999})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
def t40(request):
        a1=[]
        a2=[]
        a3=[]
        x=[]
        y=[]
        m10=[]
        request.session['m10']=m10
        n=[]
        l=[]
        o=[]
        q=[]
        r=[]
        s=[]
        t=[]
        u=[]
        a10=[]
        request.session['a10']=a10
        b10=[]
        request.session['b10']=b10
        l10=[]
        l12=[]
        s1=[]
        s2=[]
        s3=[]
        m11=[]
        request.session['m11']=m11
        m12=[]
        p=posts.objects.all().values()
        p1=privatepost.objects.all().values()
        l2=like.objects.filter(userid=request.session['userid']).values()


        for j in l10:
            l11=j['postid']
            l12.append
        for i in p.values():
            i.update({'likestatus':0})
            i.update({'commentdata':'NaN--:)'})
            i.update({'commenttime':'NaN--:)'})
            i.update({'commentstatus':0})
            i.update({'dp':'NaN--:)'})

            request.session['m10'].append(i)
        request.session['m10'].reverse()
        print(request.session['m10'])

        for i in p1.values():
            n.append(i)
        for i in request.session['m10']:
            l.append(i['postid'])
        print(l)
        for j in n:
            del j['id']
            o.append(j)
        print(o)
        print(request.session['m10'])
        xy=[]
        for m in l:
            for j in o:
                if j['postid']==m:
                   xy.append(j['userid'])
                else:
                    pass
            print(xy)
            flag=None
            for k in xy:
                if request.session['userid']==k:
                    flag=1
                    print('flag is set')
                else:
                    pass
            if flag!=1 and len(xy)>0:
                flag=0
                print('not ok')
            else:
                flag=1
            if flag==1:
                print('ok')
            else:
                print(m)
                print(request.session['m10'])
                request.session['m10']=[i for i in request.session['m10'] if not (i['postid']==m)]
            xy.clear()



        for i in request.session['m10']:
            k=i['userid']
            l=i['groupid']
            b1=bio.objects.filter(userid=k).values()
            t.append(b1)
            b2=group.objects.filter(groupid=l).values()
            u.append(b2)
        for i in t:
            for j in i.values():
                del j['userid']
                del j['mobile']
                del j['acctype']
                del j['designation']
                request.session['a10'].append(j)
        for i in u:
            for j in i.values():
                del j['groupid']
                del j['adminid']
                request.session['b10'].append(j)

        for i in l2.values():
            del i['id']
            del i['liketime']
            del i['userid']
            l10.append(i)

        for i in l10:
            for j in request.session['m10']:
                if i['postid']==j['postid']:
                    j.update({'likestatus':1})
                    s1.append(j)
        request.session['m11']=request.session['m10'].copy()
        f=comment.objects.all().values()
        for i in f.values():
            i.update({'dp':'NaN--:)'})
            a1.append(i)
        for j in request.session['m11']:
            for i in a1:
                if i['postid']==j['postid']:
                    b1=bio.objects.filter(userid=i['userid']).values()
                    for k in b1.values():
                        i.update({'dp':k['profilepic']})
                        del i['id']
                        del i['userid']
                else:
                    pass
        j1=sorted(a1,key=lambda i: (i['postid'],i['commenttime']),reverse=True)
        commentdata = {}
        commenttime = {}
        dp={}
        postid_list=[]
        for i in j1:
            if i['postid'] not in postid_list:
                postid_list.append(i['postid'])
        for j in postid_list:
            commentdata[j] = [i['commentdata']  for i in j1 if i['postid'] == j]
            commenttime[j] =[i['commenttime']  for i in j1 if i['postid'] == j]
            dp[j] =[i['dp']  for i in j1 if i['postid'] == j]
        updated_j1 = []
        for j in postid_list:
            temp_dict = {}
            temp_dict['postid'] = j
            temp_dict['commentdata'] = commentdata[j]
            temp_dict['commenttime'] = commenttime[j]
            temp_dict['dp'] = dp[j]
            updated_j1.append(temp_dict)
        for i in updated_j1:
            for j in request.session['m10']:
                if i['postid']==j['postid']:
                    j.update({'commentdata':i['commentdata']})
                    j.update({'commenttime':i['commenttime']})
                    j.update({'dp':i['dp']})
                    a3.append(j)
        request.session['m11']=request.session['m10'].copy()
        for i in request.session['m11']:
            if i['userid']==request.session['userid']:
                i['delete']=1
            else:
                pass


        for i in request.session['m11'][0:10]:
            s.append(i)
        for i in request.session['a10'][0:10]:
            x.append(i)
        for i in request.session['b10'][0:10]:
            y.append(i)
        n11=bio.objects.filter(userid=request.session['userid']).values()
        for i in n11.values():
            request.session['n12']=i['profilepic']
            request.session['n13']=i['name']

        return HttpResponse('success')
def home_lazy_content(request):#t17
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    start=request.GET.get('startpost')
    posts=[]
    users=[]
    groups=[]

    end=int(start)+10
    if(check(useid,token)):
        finaldict1={}

        for i in request.session['m11'][int(start):end]:
            posts.append(i)
        for i in request.session['a10'][int(start):end]:
            users.append(i)
        for i in request.session['b10'][int(start):end]:
            groups.append(i)
        context={
                'post':posts,
                'user':users,
                'group':groups
            }


        finaldict1.update({'status':2})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':context})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':999})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))

@csrf_exempt
def like_save(request):#t18
    finaldict1={}
    useid=int(request.headers['X-User'])
    token=request.headers['X-Token']
    j=[]
    k=[]
    if(check(useid,token)):
        postid=request.POST.get('postid')
        likestatus=request.POST.get('likestatus')
        #print(postid)
        #print(likestatus)
        now=datetime.datetime.now()
        t=now.strftime("%d/%m/%y %H:%M:%S")
        #print(t)
        if likestatus=='1':
            l3=like.objects.filter(postid=postid).all().values()
            for i in l3.values():
                del i['id']
                j.append(i)
            #print(j)
            if len(j)==0:
                l5=like(postid=postid,userid=useid,liketime=t)
                l5.save()
                #print('len saved')
            else:
                for i in j:
                    print(i['postid'])
                    print(int(postid))
                    print(i['userid'])

                    if (i['postid']==int(postid)) and (i['userid']==useid):
                        #print('same pu')
                        pass
                    else:
                        l5=like(postid=postid,userid=useid,liketime=t)
                        l5.save()
                        #print('else saved')
                        break
        else:
            l6=like.objects.filter(postid=postid).filter(userid=useid).delete()
        l4=like.objects.filter(postid=postid).all().values()
        for i in l4.values():
           k.append(i['postid'])
        #print(k)
        x=len(k)
        #print('count',x)
        p2=posts.objects.filter(postid=postid).values()
        for i in p2.values():
            p1id=i['postid']
            u1id=i['userid']
            gp1id=i['groupid']
            pd1=i['postdata']
            img1=i['fileurl']
            pttime=i['posttime']
            exten=i['extension']
            filesize=i['filesize']
        p3=posts(postid=p1id,userid=u1id,groupid=gp1id,postdata=pd1,fileurl=img1,posttime=pttime,likecount=x,extension=exten,filesize=filesize)
        p3.save()

        return HttpResponse(1)
    else:

        return HttpResponse(999)

@csrf_exempt
def t19(request):#t19
    j=[]
    k=[]
    postid=request.POST.get('postid')
    likestatus=request.POST.get('likestatus')
    now=datetime.datetime.now()
    t=now.strftime("%d/%m/%y %H:%M:%S")
    if likestatus=='1':
        l3=like.objects.filter(postid=postid).values()
        for i in l3.values():
            del i['id']
            j.append(i)
        if len(j)==0:
            l5=like(postid=postid,userid=request.session['userid'],liketime=t)
            l5.save()
            print('len saved')
        else:
            for i in j:
                print(i['postid'])
                print(i['userid'])
                if i['postid']==postid and i['userid']==request.session['userid']:
                    print('same')
                    pass
                else:
                    l5=like(postid=postid,userid=request.session['userid'],liketime=t)
                    l5.save()
                    print('else part saved')

    else:
        l6=like.objects.filter(postid=postid).filter(userid=request.session['userid']).delete()
    l4=like.objects.filter(postid=postid).all().values()
    for i in l4.values():
       k.append(i['postid'])
    print(k)
    x=len(k)
    print(x)
    p2=posts.objects.filter(postid=postid).values()
    for i in p2.values():
        p1id=i['postid']
        u1id=i['userid']
        gp1id=i['groupid']
        pd1=i['postdata']
        img1=i['fileurl']
        pttime=i['posttime']
    p3=posts(postid=p1id,userid=u1id,groupid=gp1id,postdata=pd1,fileurl=img1,posttime=pttime,likecount=x)
    p3.save()
    return HttpResponse('sucess')

@csrf_exempt
def privatereply_save(request):#t20
    now=datetime.datetime.now()
    t=now.strftime("%d/%m/%y %H:%M:%S")
    idto=request.POST.get('reply_to')
    postid=request.POST.get('post_id')
    replydata=request.POST.get('replydata')
    r=privatereply(idfrom=request.session['userid'],idto=idto,replydata=replydata,replytime=t,postid=postid)
    r.save()
    return HttpResponse('success')

@csrf_exempt
def comment_save(request):#t21
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    if(check(useid,token)):
        now=datetime.datetime.now()
        t=now.strftime("%d/%m/%y %H:%M:%S")
        postid=request.POST.get('postid')
        commentdata1=request.POST.get('commentdata')
        commentdata=commentdata1.encode('unicode-escape').decode('utf-8')
        c=comment(postid=postid,userid=useid,commentdata=commentdata,commenttime=t)
        c.save()
        return HttpResponse(1)
    else:
        return HttpResponse(999)
def group_post_filter(request):#t24
    finaldict1={}
    gpinfo={}
    gdata=request.GET.get('getgroupdata')
    fgrpid=request.GET.get('gid1')
    #print('******************',fgrpid)
    if(fgrpid==None):
        pass
    else:
        request.session['gid1']=int(fgrpid)
        #print('******************',fgrpid)
        #print( 'in else t24-----',request.session['gid1'])
    g1=group.objects.filter(groupid=fgrpid).values()
    for data in g1.values():
        gpinfo.update(data)
    w=[]
    request.session['w']=w
    x1=[]
    request.session['x1']=x1
    x2=[]
    request.session['x2']=x2
    x3=[]
    x4=[]
    x5=[]


    for i in request.session['m11']:
        if request.session['gid1']==i['groupid']:
            request.session['w'].append(i)
    #print('/////',request.session['w'])
    for i in request.session['w']:
        b12=bio.objects.filter(userid=i['userid']).values()
        for j in b12.values():
            del j['acctype']
            del j['mobile']
            del j['designation']
            request.session['x1'].append(j)
    for i in request.session['m11']:
        if request.session['gid1']==i['groupid']:
            g11=group.objects.filter(groupid=request.session['gid1']).values()
            for j in g11.values():
                del j['adminid']
                # del j['groupid']
                request.session['x2'].append(j)

    z2=len(request.session['w'])
    for i in request.session['w'][0:10]:
        x3.append(i)
    for i in request.session['x1'][0:10]:
        x4.append(i)
    for i in request.session['x2'][0:10]:
        x5.append(i)
    #print(z2)
    context={

            'post':x3,
            'user':x4,
            'group':x5,
            'userdp':request.session['n12'],
            'username':request.session['n13'],
            'groupinfo':gpinfo,
            'length':z2
        }
    #print(context)

    finaldict1.update({'status':3})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':context})
    return HttpResponse(json.dumps(finaldict1))

def iterate_group_post_filter(request):#t25

    finaldict1 = {}
    startpost = request.GET.get('startpost')
    startIndex = int(startpost)
    endIndex = startIndex + 10

    #print(startIndex)

    posts = []
    users = []
    groups = []

    for i in request.session['w'][startIndex:endIndex]:
        posts.append(i)
    for i in request.session['x1'][startIndex:endIndex]:
        users.append(i)
    for i in request.session['x2'][startIndex:endIndex]:
        groups.append(i)

    context={
        'post':posts,
        'user':users,
        'group':groups,
    }

    finaldict1.update({'status':2})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':context})

    return HttpResponse(json.dumps(finaldict1))

def groupdetails(request):#t26
    rinfo=request.GET.get('requestinfo')
    x3=[]
    fgrpid=request.GET.get('gid1')
    #print('******************',fgrpid)
    if(fgrpid==None):
        pass
    else:
        request.session['gid1']=int(fgrpid)
        #print('******************',fgrpid)
        #print( 'in else t24-----',request.session['gid1'])

    #print(request.session['gid1'])
    if rinfo=='1':
        g15=group.objects.filter(groupid=request.session['gid1']).values()
        for j in g15.values():
            del j['adminid']
            del j['groupid']
            x3.append(j)
            break
        #print(x3)
        return HttpResponse(json.dumps(x3))
    else:
        #print("ele")
        pass
def t27(request):
    lout=request.GET.get('logout')
    if lout=='1':
        d9=logout.objects.filter(userid=request.session['userid']).update(lflag=1)
        #print('success flag changed')
        request.session.flush()
        return HttpResponse(json.dumps('success'))
    else:
        pass
def t28(request):
    req=request.GET.get('request')
    s=[]
    if req=='1':
        d1=darkmode.objects.filter(userid=request.session['userid']).values()
        for i in d1.values():
            del i['id']
        s.append(i)
        print(s)
        return HttpResponse(json.dumps(s))
    else:
        pass
def t29(request):
    dark=request.GET.get('dark')
    request.session['dark']=dark
    #print(request.session['dark'])
    d2=darkmode.objects.filter(userid=request.session['userid']).update(dark=request.session['dark'])
    return HttpResponse('success')
def userdetails(request):#t32
    req=request.GET.get('request')
    if req=='1':
        x1=[]
        v1=bio.objects.filter(userid=request.session['userid']).values()
        for i in v1:
            del i['acctype']

            x1.append(i)
        return HttpResponse(json.dumps(x1))
    else:
        pass
def t33(request):
    nc=request.GET.get('notificationcount')
    if nc=='1':
        n1=notificationcount.objects.filter(userid=request.session['userid']).values()
        for i in n1.values():
            print(i['nocount'])
            i['nocount']=int(i['nocount'])+1
            n2=notificationcount.objects.filter(userid=request.session['userid']).update(nocount=i['nocount'])
        return HttpResponse('success')
    else:
        pass
def init_notification(request):#t34
    finaldict1={}
    nt=request.GET.get('notificationtime')
    useid=request.headers['X-User']
    request.session['userid']=int(useid)
    if nt=='1':
        now=datetime.datetime.now()
        t=now.strftime("%d/%m/%y %H:%M:%S")
        #print(t)
        n3=notificationcount.objects.filter(userid=request.session['userid']).values()
        for i in n3.values():
            if i['nocount']==1:
                p=posts.objects.all().values()
                p1=privatepost.objects.all().values()
                templist=[]
                n=[]
                l=[]
                o=[]

                for i in p.values():
                    if(i["fileurl"]==None or i["fileurl"]=='NULL'):
                        del i["fileurl"]
                        del i["extension"]
                        del i["filesize"]
                    elif(i['extension']!="png" or i['extension']!="jpeg" or i['extension']!="jpg" or i['extension']!="gif" or i['extension']!="jfif"):
                        del i["fileurl"]
                        del i["extension"]
                        del i["filesize"]
                    else:
                        del i["extension"]
                        del i["filesize"]
                    ud=bio.objects.filter(userid=i['userid']).values()
                    for data in ud.values():
                        i.update({'name':data['name']})
                        i.update({'dp':data['profilepic']})
                    gd=group.objects.filter(groupid=i['groupid']).values()
                    for data in gd.values():
                        i.update({'gname':data['groupname']})
                    i.update({'type':'post'})
                    i.update({'notificationContent':'has posted in'})
                    templist.append(i)
                templist.reverse()
                #print(p1)
                for i in p1.values():
                    n.append(i)
                for i in templist:
                    l.append(i['postid'])
                #print(l)
                for j in n:
                    del j['id']
                    o.append(j)
                #print(o)
                #print(templist)
                xy=[]
                for m in l:
                    for j in o:
                        if j['postid']==m:
                           xy.append(j['userid'])
                        else:
                            #print('postid diffErent')
                            pass
                    #print(xy)
                    flag=None
                    for k in xy:
                        if request.session['userid']==k:
                            flag=1
                            #print('flag is set')
                        else:
                            pass
                    if flag!=1 and len(xy)>0:
                        flag=0
                        #print('not ok')
                    else:
                        flag=1
                    if flag==1:
                        print('ok')
                    else:
                        #print(m)
                        #print(templist)
                        templist=[i for i in templist if not (i['postid']==m)]
                    xy.clear()
                j10=sorted(templist,key=lambda i: (i['posttime']),reverse=True)
                #print(templist)
                n4=ntime.objects.filter(userid=request.session['userid']).update(ptime=t)
                n5=ntime.objects.filter(userid=request.session['userid']).update(etime=t)
                #print('in n5')


                a1=[]
                r1=privatereply.objects.filter(idto=request.session['userid']).values()
                for i in r1.values():
                    del i['idto']
                    del i['replydata']
                    i.update({'type':'reply'})
                    r2=bio.objects.filter(userid=i['idfrom']).values()
                    for j in r2.values():
                        i.update({'name':j['name']})
                        i.update({'dp':j['profilepic']})
                    r3=posts.objects.filter(postid=i['postid']).values()
                    for k in r3.values():
                        r4=group.objects.filter(groupid=k['groupid']).values()
                        for l in r4.values():
                            i.update({'gname':l['groupname']})
                    del i['idfrom']
                    del i['postid']
                    a1.append(i)
                j8=sorted(a1,key=lambda i: (i['replytime']),reverse=True)
                a2=[]
                r5=comment.objects.all().values()
                for i in r5.values():
                    i.update({'type':'comment'})
                    i.update({'notificationContent':'has commented to your post in'})
                    r8=bio.objects.filter(userid=i['userid']).values()
                    for l in r8.values():
                        i.update({'name':l['name']})
                        i.update({'dp':l['profilepic']})
                    r6=posts.objects.filter(postid=i['postid']).values()
                    for j in r6.values():
                        if j['userid']==request.session['userid']:
                            r7=group.objects.filter(groupid=j['groupid']).values()
                            for k in r7.values():
                                i.update({'gname':k['groupname']})
                            del i['commentdata']
                            del i['postid']
                            a2.append(i)
                            #print(a2)
                            a2=[i for i in a2 if not (i['userid']==request.session['userid'])]
                            #print(a2)
                        else:
                            pass
                j6=sorted(a2,key=lambda i: (i['commenttime']),reverse=True)

                a3=[]
                r9=like.objects.all().values()
                for i in r9.values():
                    del i["id"]
                    i.update({'type':'like'})
                    i.update({'notificationContent':'has liked your post in'})
                    r11=bio.objects.filter(userid=i['userid']).values()
                    for l in r11.values():
                        i.update({'userid':l['userid']})
                        i.update({'name':l['name']})
                        i.update({'dp':l['profilepic']})
                    r10=posts.objects.filter(postid=i['postid']).values()
                    for j in r10.values():
                        if j['userid']==request.session['userid']:
                            i.update({'postid':j['postid']})
                            i.update({'likecount':j['likecount']})
                            r12=group.objects.filter(groupid=j['groupid']).values()
                            for k in r12.values():
                                i.update({'groupid':k['groupid']})
                                i.update({'gname':k['groupname']})
                            del i['postid']
                            a3.append(i)
                            a3=[i for i in a3 if not (i['userid']==request.session['userid'])]
                j7=sorted(a3,key=lambda i: (i['liketime']),reverse=True)
                a6=[]
                for i in j8:
                    k='replytime'
                    j='commenttime'
                    i[j]=i.pop(k)
                    a6.append(i)
                a7=[]
                for i in j7:
                    k='liketime'
                    j='commenttime'
                    i[j]=i.pop(k)
                    a7.append(i)
                p11=[]
                for i in templist:
                    k='posttime'
                    j='commenttime'
                    i[j]=i.pop(k)
                    p11.append(i)
                a5=[]
                a5=a6+a7+j6+templist
                #print(a5)
                j9=sorted(a5,key = lambda x: datetime.datetime.strptime(x['commenttime'], '%d/%m/%y %H:%M:%S'))
                for data in j9:
                    data.update({'isnew':1})
                    del data['commenttime']
                    del data['userid']
                    del data['likecount']
                    del data['groupid']

                j9.reverse()
                context={
                    'content':j9
                }
                finaldict1.update({'status':6})
                finaldict1.update({'message':'success'})
                finaldict1.update({'data':context})
                return HttpResponse(json.dumps(finaldict1))
            else:
                now=datetime.datetime.now()
                t=now.strftime("%d/%m/%y %H:%M:%S")
                n5=ntime.objects.filter(userid=request.session['userid']).values()
                p=posts.objects.all().values()
                p1=privatepost.objects.all().values()
                templist=[]
                n=[]
                l=[]
                o=[]

                for i in p.values():
                    if(i['fileurl']==None or i['fileurl']=='NULL'):
                        del i["fileurl"]
                        del i["extension"]
                        del i["filesize"]
                    elif(i['extension']!="png" and i['extension']!="jpeg" and i['extension']!="jpg" and i['extension']!="gif" and i['extension']!="jfif"):
                        del i["fileurl"]
                        del i["extension"]
                        del i["filesize"]
                    else:
                        del  i["extension"]
                        del i["filesize"]
                    ud=bio.objects.filter(userid=i['userid']).values()
                    for data in ud.values():
                        i.update({'name':data['name']})
                        i.update({'dp':data['profilepic']})
                    gd=group.objects.filter(groupid=i['groupid']).values()
                    for data in gd.values():
                        i.update({'gname':data['groupname']})
                    i.update({'type':'post'})
                    i.update({'notificationContent':'has posted in'})
                    del i['postdata']
                    templist.append(i)
                templist.reverse()
                #print(p1)
                for i in p1.values():
                    n.append(i)
                for i in templist:
                    l.append(i['postid'])
                print(l)
                for j in n:
                    del j['id']
                    o.append(j)
                #print(o)
                #print(templist)
                xy=[]
                for m in l:
                    for j in o:
                        if j['postid']==m:
                           xy.append(j['userid'])
                        else:
                            #print('postid diffErent')
                            pass
                    #print(xy)
                    flag=None
                    for k in xy:
                        if request.session['userid']==k:
                            flag=1
                            #print('flag is set')
                        else:
                            pass
                    if flag!=1 and len(xy)>0:
                        flag=0
                        print('not ok')
                    else:
                        flag=1
                    if flag==1:
                        print('ok')
                    else:
                        #print(m)
                        #print(templist)
                        templist=[i for i in templist if not (i['postid']==m)]
                    xy.clear()
                j10=sorted(templist,key=lambda i: (i['posttime']),reverse=True)
                for i in n5.values():
                    n7=ntime.objects.filter(userid=request.session['userid']).update(ptime=i['etime'])
                    n6=ntime.objects.filter(userid=request.session['userid']).update(etime=t)
                a1=[]
                r1=privatereply.objects.filter(idto=request.session['userid']).values()
                for i in r1.values():
                    del i['idto']
                    del i['replydata']
                    i.update({'type':'reply'})
                    r2=bio.objects.filter(userid=i['idfrom']).values()
                    for j in r2.values():
                        i.update({'name':j['name']})
                        i.update({'dp':j['profilepic']})
                    r3=posts.objects.filter(postid=i['postid']).values()
                    for k in r3.values():
                        r4=group.objects.filter(groupid=k['groupid']).values()
                        for l in r4.values():
                            i.update({'gname':l['groupname']})
                    del i['idfrom']
                    del i['postid']
                    a1.append(i)
                j8=sorted(a1,key=lambda i: (i['replytime']),reverse=True)
                a2=[]
                r5=comment.objects.all().values()

                for i in r5.values():
                    del i["id"]
                    i.update({'type':'comment'})
                    i.update({'notificationContent':'has commented to your post in'})
                    r8=bio.objects.filter(userid=i['userid']).values()
                    for l in r8.values():
                        i.update({'userid':l['userid']})
                        i.update({'name':l['name']})
                        i.update({'dp':l['profilepic']})
                    r6=posts.objects.filter(postid=i['postid']).values()
                    for j in r6.values():

                        if (j['userid']==request.session['userid']):
                            r7=group.objects.filter(groupid=j['groupid']).values()
                            for k in r7.values():
                                i.update({'groupid':k['groupid']})
                                i.update({'gname':k['groupname']})

                            del i['commentdata']
                            i.update({'likecount':j['likecount']})
                            if(j['extension']=="png" or j['extension']=="jpeg" or j['extension']=="jpg" or j['extension']=="gif" or j['extension']=="jfif"):
                                i.update({"fileurl": j["fileurl"]})

                            a2.append(i)
                            #print('.,.,.,.,.,.,.,.,a2',a2)
                            a2=[i for i in a2 if not (i['userid']==request.session['userid'])]
                        else:
                            pass
                j6=sorted(a2,key=lambda i: (i['commenttime']),reverse=True)
                #print('.,.,.,.,.,.,.,.,',j6)
                a3=[]
                r9=like.objects.all().values()
                for i in r9.values():
                    del i["id"]
                    i.update({'type':'like'})
                    i.update({'notificationContent':'has liked your post in'})
                    r11=bio.objects.filter(userid=i['userid']).values()
                    for l in r11.values():
                        i.update({'userid':l['userid']})
                        i.update({'name':l['name']})
                        i.update({'dp':l['profilepic']})
                    r10=posts.objects.filter(postid=i['postid']).values()
                    for j in r10.values():

                        if (j['userid']==request.session['userid']):

                            i.update({'likecount':j['likecount']})
                            r12=group.objects.filter(groupid=j['groupid']).values()

                            for k in r12.values():
                                i.update({'groupid':k['groupid']})
                                i.update({'gname':k['groupname']})

                            a3.append(i)

                            a3=[i for i in a3 if not (i['userid']==request.session['userid'])]


                j7=sorted(a3,key=lambda i: (i['liketime']),reverse=True)

                a6=[]
                for i in j8:
                    k='replytime'
                    j='commenttime'
                    i[j]=i.pop(k)
                    a6.append(i)
                a7=[]
                for i in j7:
                    k='liketime'
                    j='commenttime'
                    i[j]=i.pop(k)
                    a7.append(i)
                p11=[]
                for i in j10:
                    k='posttime'
                    j='commenttime'
                    i[j]=i.pop(k)
                    p11.append(i)
                a5=[]
                a5=a6+a7+j6+p11
                #print('???????????',a5)
                j9=sorted(a5,key = lambda x: datetime.datetime.strptime(x['commenttime'], '%d/%m/%y %H:%M:%S'))
                #print(j9)

                latest=[]
                earlier=[]
                n10=ntime.objects.filter(userid=request.session['userid']).values()
                for j in n10.values():
                    for i in j9:
                        if i['commenttime']>j['ptime'] and i['commenttime']<j['etime'] :

                            i.update({'isnew':1})
                            #latest.append(i)
                        else:

                            i.update({'isnew':0})
                            #earlier.append(i)
                #earlier.reverse()
                for data in j9:
                    del data['commenttime']
                    del data['userid']
                    del data['likecount']
                    del data['groupid']


                j9.reverse()
                context={

                    'content':j9

                }
                finaldict1.update({'status':6})
                finaldict1.update({'message':'success'})
                finaldict1.update({'data':context})
                return HttpResponse(json.dumps(finaldict1))



@csrf_exempt
def t35(request):
    typ=request.POST.get('type')
    request.session['typ']=typ
    did=request.POST.get('id')
    request.session['did']=did
    return HttpResponse('success')


def lc(request,did):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'notifications_comment.html',{'s':s})


def rep(request,did):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'notifications_reply.html',{'s':s})

"""
type post is pending
"""

def notification_content(request):#t36
    did=request.GET.get('nofid')
    type_1=request.GET.get('type')
    finaldict1={}
    userid=request.headers['X-User']
    token=request.headers['X-Token']
    if(did!=''and did!=None and type_1!='' and type_1!=None and userid!='' and userid!=None):
        request.session['did']=int(did)
        request.session['typ']=type_1
        request.session['userid']=int(userid)
    else:
        pass
    if check(userid,token):
        x1=[]
        x2=[]
        if request.session['typ']=='like':
            l1=like.objects.filter(id=request.session['did']).values()
            for i in l1.values():
                l2=posts.objects.filter(postid=i['postid']).values()
                for j in l2.values():
                    l3=bio.objects.filter(userid=j['userid']).values()
                    for k in l3.values():
                        j.update({'name':k['name']})
                    l9=group.objects.filter(groupid=j['groupid']).values()
                    for o in l9.values():
                        j.update({'groupname':o['groupname']})
                        j.update({'gdp':o['groupdp']})
                    x1.append(j)
                    l4=comment.objects.filter(postid=j['postid']).values()
                    for m in l4.values():
                        l5=bio.objects.filter(userid=m['userid']).values()
                        for n in l5.values():
                            m.update({'cdp':n['profilepic']})
                            x2.append(m)


                for i in x1:
                    print(i)

                    for j in request.session['m11']:

                        if i['postid']==j['postid'] and j['userid']==request.session['userid']:
                            i.update({'likestatus':j['likestatus']})
                            i.update({'delete':j['delete']})
                            i.update({'commentstatus':0})

                        else:
                            pass

            z5=[]
            z10=bio.objects.filter(userid=request.session['userid']).values()
            for i in z10.values():
                z5.append(i['profilepic'])
            context={
                'pdata':x1,
                'cdata':x2,
                'logindp':z5,

            }
            finaldict1.update({'status':'success'})
            finaldict1.update({'message':'success'})
            finaldict1.update({'data':context})
            return HttpResponse(json.dumps(finaldict1))
        elif request.session['typ']=='comment':
            c1=comment.objects.filter(id=request.session['did']).values()
            y1=[]
            y2=[]
            y3=[]
            y4=[]

            for i in c1.values():
                c2=posts.objects.filter(postid=i['postid']).values()
                for j in c2.values():
                    c3=bio.objects.filter(userid=j['userid']).values()
                    for k in c3.values():
                        j.update({'name':k['name']})
                    c4=group.objects.filter(groupid=j['groupid']).values()
                    for l in c4.values():
                        j.update({'groupname':l['groupname']})
                        j.update({'gdp':l['groupdp']})
                    y1.append(j)
                    c5=comment.objects.filter(postid=i['postid']).values()
                    for m in c5.values():
                        c6=bio.objects.filter(userid=m['userid']).values()
                        for n in c6.values():
                            m.update({'cdp':n['profilepic']})
                        if int(m['id'])==int(request.session['did']):
                            y2.append(m)
                        else:
                            y3.append(m)

            y4=[]
            y4=y2+y3

            for i in y1:
                for j in request.session['m11']:

                    if i['postid']==j['postid'] and j['userid']==request.session['userid']:
                        i.update({'likestatus':j['likestatus']})
                        i.update({'delete':j['delete']})
                        i.update({'commentstatus':1})
                    else:
                        pass
            z5=[]
            z10=bio.objects.filter(userid=request.session['userid']).values()
            for i in z10.values():
                z5.append(i['profilepic'])
            context={
                'pdata':y1,
                'cdata':y4,
                'logindp':z5
            }
            finaldict1.update({'status':'success'})
            finaldict1.update({'message':'success'})
            finaldict1.update({'data':context})
            return HttpResponse(json.dumps(finaldict1))
        else:
            r1=privatereply.objects.filter(id=request.session['did']).values()
            z1=[]
            z2=[]
            z3=[]
            z4=[]
            for i in r1.values():
                r9=bio.objects.filter(userid=i['idfrom']).values()
                for p in r9.values():
                    z4.append(p['profilepic'])
                r2=posts.objects.filter(postid=i['postid']).values()
                for j in r2.values():
                    r3=bio.objects.filter(userid=j['userid']).values()
                    for k in r3.values():
                        j.update({'name':k['name']})
                    r4=group.objects.filter(groupid=j['groupid']).values()
                    for l in r4.values():
                        j.update({'groupname':l['groupname']})
                        j.update({'gdp':l['groupdp']})
                    z1.append(j)
                    z2.append(i['replydata'])
                    r7=comment.objects.filter(postid=i['postid']).values()
                    for m in r7.values():
                        r8=bio.objects.filter(userid=m['userid']).values()
                        for n in r8.values():
                            m.update({'cdp':n['profilepic']})
                        z3.append(m)
            for i in z1:
                for j in request.session['m11']:
                    #print(j['userid'])
                    if i['postid']==j['postid'] and j['userid']==request.session['userid']:
                        i.update({'likestatus':j['likestatus']})
                        i.update({'delete':j['delete']})
                    else:
                        pass

            z5=[]
            z10=bio.objects.filter(userid=request.session['userid']).values()
            for i in z10.values():
                z5.append(i['profilepic'])
            context={
                'pdata':z1,
                'cdata':z3,
                'rdata':z2,
                'rdp':z4,
                'logindp':z5
            }
            finaldict1.update({'status':'success'})
            finaldict1.update({'message':'success'})
            finaldict1.update({'data':context})
            return HttpResponse(json.dumps(finaldict1))



def up(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'userprofile.html',{'s':s})



def about(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'about.html',{'s':s})



def signup1(request):
    return render(request,'signup1.html')



def target(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'target.html',{'s':s})



def target1(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'target1.html',{'s':s})



def signup(request):
    return render (request,'signup.html')



def signup2(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'signup2.html',{'s':s})



def accountcreated(request):
    b2=bio.objects.filter(userid=request.session['userid']).values()
    for i in b2.values():
        del i['userid']
        del i['acctype']
        del i['designation']
        del i['profilepic']
    n=i['name']
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'accountcreated.html',{'n':n,'s':s})



def notifications(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'notifications.html',{'s':s})



def home(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    print(s)
    return render (request,'home.html',{'s':s})

def search(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'search.html',{'s':s})



def post(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'post.html',{'s':s})



def tag(request):
    return render (request,'tag.html')



def comments(request):
    return render (request,'comments.html')



def view_members(request):
    return render (request,'view_members.html')



def settings(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'settings.html',{'s':s})


def create_group(request):
    return render (request,'create_group.html')



def groups(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render (request,'groups.html',{'s':s})



def more(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'groups_more.html',{'s':s})


def editprofdp(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'editprofdp.html',{'s':s})


@csrf_exempt
def post_delete(request):#t41
    finaldict1={}
    del1=request.POST.get('deletepost')
    print(del1)
    if del1=='1':
        pid=request.POST.get('postid')
        #print(pid)
        d6=posts.objects.filter(postid=pid).values()
        #print(d6)
        for data in d6.values():
            deldata=data['fileurl']
        #print(deldata)
        d1=posts.objects.filter(postid=pid).delete()
        d2=comment.objects.filter(postid=pid).delete()
        d3=like.objects.filter(postid=pid).delete()
        d4=privatereply.objects.filter(postid=pid).delete()
        d5=privatepost.objects.filter(postid=pid).delete()
        print("post deleted")
        if(deldata=='NULL' or deldata==None or deldata==''):
            print('datanull')
        else:
            print('not null')
            os.remove("/home/mectmoment/Moment/mectapp/"+deldata)
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(1)
    else:
        finaldict1.update({'status':'failed'})
        finaldict1.update({'message':'delete variable not set'})
        finaldict1.update({'data':{}})
        return HttpResponse(0)


def cpass(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'changepassword.html',{'s':s})

@csrf_exempt
def changepassword(request):#t42
    finaldict={}
    password=request.POST.get('currentpassword')
    npassword=request.POST.get('newpassword')
    userid_1=request.headers['X-User']
    token=request.headers['X-Token']
    if(check(userid_1,token)):
        if(userid_1!='' and userid_1!=None):
            request.session['userid']=int(userid_1)
        pa1=userid.objects.filter(userid=request.session['userid'])
        for i in pa1.values():
            l=i['password']
            enc=pbkdf2_sha256.verify(password,l)
            if enc==True:
                print('password true')
                pw=enc=pbkdf2_sha256.hash(str(npassword))
                print('hashedpassword----------------',pw)
                pa1=userid.objects.filter(userid=request.session['userid']).update(password=pw)
                print('passwd updated')

                return HttpResponse(1)
            else:

                return HttpResponse(0)
    else:

        return HttpResponse(0)

@csrf_exempt
def password_save(request):#t43
    finaldict={}
    password=request.POST.get('newpassword')
    print('changed password----------------',password)
    userid_1=request.headers['X-User']
    token=request.headers['X-Token']
    if(check(userid_1,token)):
        if(userid_1!='' and userid_1!=None):
            request.session['userid']=int(userid_1)
        pw=enc=pbkdf2_sha256.hash(str(password))
        print('hashedpassword----------------',pw)
        pa1=userid.objects.filter(userid=request.session['userid']).update(password=pw)
        print('passwd updated')
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))

def wardinfo(request):
    useid=int(request.headers['X-User'])
    finaldict1={}
    userdet=[]
    user={}
    studentid=[]
    tut=td.objects.filter(staff=useid).values()
    for data in tut.values():
        studentid.append(data['student'])
    for data in studentid:
        biodet=bio.objects.filter(userid=data).values()
        for data1 in biodet.values():
            user.update(data1)

            userdet.append(user)
            user={}
    finaldict1.update({'status':4})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':userdet})
    return HttpResponse(json.dumps(finaldict1))

def isstaff(id):
    b1=bio.objects.filter(userid=id).values()
    for data in b1.values():
        if(data['acctype']==0):
            return 1
        else:
            return 0

def profiledetails(request):
    useid=int(request.GET.get('userid'))
    userid_1=int(request.headers['X-User'])
    token=request.headers['X-Token']
    if(check(userid_1,token)):
        finaldict1={}
        user={}
        user.update({'userid':useid})
        u1=userid.objects.filter(userid=useid).values()
        for data in u1.values():
            user.update({'useremail':data['email']})
        u2=bio.objects.filter(userid=useid).values()
        for data in u2.values():
            user.update({'name':data['name']})
            user.update({'profilepic':data['profilepic']})
            #print('~~~~',useid,userid_1, isstaff(useid),isstaff(userid_1))
            if(useid==userid_1 or isstaff(useid)==1 or isstaff(userid_1)==1):
                user.update({'usermobile':data['mobile']})

            else:
                 user.update({'usermobile':None})
            user.update({'reg_no':data['reg_no']})
            if(data['altemail']==None or data['altemail']==''):
                user.update({'altemail':None})
            else:
                user.update({'altemail':None})
        u3=td.objects.filter(student=useid).values()
        if(len(u3)==0):
            user.update({'tutorname':'Not updated'})
        else:
            for data in u3.values():
                b1=bio.objects.filter(userid=data['staff']).values()
                for data1 in b1.values():
                    user.update({'tutorname':data1['name']})
        finaldict1.update({'status':5})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':user})
        return HttpResponse(json.dumps(finaldict1))
def add_tutor(request):#t44
    finaldict1={}
    y=[]
    z=[]
    z1=[]
    target=request.GET.get('target')
    if target=='1':
        l1=bio.objects.filter(userid=request.session['userid']).values()
        for l in l1.values():
                k2=bio.objects.filter(acctype=0).exclude(designation=0).values()
                for k in k2.values():
                    del k['mobile']
                    del k['acctype']
                    del k['designation']
                    z.append(k)
                for i in z:
                    if i['userid']==request.session['userid']:
                        del i['userid']
                        del i['name']
                        del i['profilepic']
                    else:
                        z1.append(i)

        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':z1})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'failed'})
        finaldict1.update({'message':'target variable not set'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))

def tutor(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    b2=bio.objects.filter(userid=request.session['userid']).values()
    for i in b2.values():
        del i['userid']
        del i['acctype']
        del i['designation']
        del i['profilepic']
    n=i['name']
    b10=td.objects.filter(student=request.session['userid']).values()
    for i in b10.values():
        print(len(i))
    if len(i)==4:
        b8=td.objects.filter(student=request.session['userid']).values()
        for j in b8.values():
            del j['student']
            del j['addflag']
        k1=j['staff']
        b9=bio.objects.filter(userid=k1).values()
        for i in b9.values():
            del i['userid']
            del i['acctype']
            del i['designation']
            del i['profilepic']
        k=i['name']
        return render(request,'info.html',{'n':n,'s':s,'k':k})
    else:
        return render(request,'tutor.html',{'s':s})


@csrf_exempt
def tutor_save(request):#t45
    firstdict1={}
    userid_1=request.headers['X-User']
    token=request.headers['X-Token']
    tutid=request.POST.get('tutorid')
    request.session['userid']=userid_1
    tokens=[]
    apikey="AAAA-_B-JEI:APA91bGTzkC8n_fsX0NuoQY5p7xY4iDzhOXmmKuX1Fr6Mtwbnl3CZNPle-8S17Bs-v3leYrjMesUl4Xy8FdZVVsYkHQI5k-6Dspd1XtUVtfwiliNTiXQu4EuAAp6_bYK0BY6oCl0OLND"
    if(tutid!='' or tutid!=None):
        si=int(tutid)
        #print(si)
        n2=td(staff=si,student=request.session['userid'],addflag=1)
        n2.save()
        b1=bio.objects.filter(userid=si).values()
        for data in b1.values():
            name=data["name"].split(" ")
            name1=""
            for d in name:
                name1=name1+d
        f1=fcmdata.objects.filter(userid=userid_1).values()
        for data in f1.values():
            fcm=data['fcmtoken']
            tokens.append(data['fcmtoken'])
        if(topicsubscription(apikey,tokens,"tutor_"+str(si)+"_"+str(name1))==1):#tutor_id_name
            #print("tutor_",si,name)
            now=datetime.datetime.now()
            t=now.strftime("%d/%m/%y %H:%M:%S")
            ftoken=fcmdata(userid=userid_1,fcmtoken=fcm,topics_subscribed="tutor_"+str(si)+"_"+str(name1),time_sub=t)
            ftoken.save()
        print('tutor added')
    '''else:
        if len(p2)==0:
            pass
        else:
            for i in p2:
                si=int(i)
            print(si)
            n2=td(staff=si,student=request.session['userid'],addflag=1)
            n2.save()
            print('tutor added')'''
    return HttpResponse(1)



def info(request):
    b2=bio.objects.filter(userid=request.session['userid']).values()
    for i in b2.values():
        del i['userid']
        del i['acctype']
        del i['designation']
        del i['profilepic']
    n=i['name']
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    b8=td.objects.filter(student=request.session['userid']).values()
    for j in b8.values():
        del j['student']
        del j['addflag']
    k1=j['staff']
    b9=bio.objects.filter(userid=k1).values()
    for i in b9.values():
        del i['userid']
        del i['acctype']
        del i['designation']
        del i['profilepic']
    k=i['name']
    return render (request,'info.html',{'n':n,'s':s,'k':k})


def t46(request):
    req=request.GET.get('request_1')
    if req=='1':
        use=request.session['userid']
        return HttpResponse(json.dumps(use))
    else:
        pass
def settings1(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'settings1.html')



@csrf_exempt
def tutor_member_list(request):#t47
    finaldict1={}
    y=[]
    z=[]
    z1=[]
    z2=[]
    z3=[]
    userid_1=request.headers['X-User']
    token=request.headers['X-Token']
    if(userid_1!='' and userid_1!=None):
        request.session['userid']=int(userid_1)

    if(check(userid_1,token)):
        l1=bio.objects.filter(userid=request.session['userid']).values()
        for l in l1.values():
            if(l['acctype']==0):
                k2=td.objects.filter(staff=request.session['userid']).values()
                for k in k2.values():
                    del k['addflag']
                    del k['id']
                    z.append(k)
                for i in z:
                    l3=bio.objects.filter(userid=i['student']).values()
                    for j in l3.values():
                        del j['mobile']
                        del j['acctype']
                        del j['designation']
                        z1.append(j)
                z3.append(request.session['p'])
                z2.append(request.session['userid'])
                z4={
                    'tutor':z1,
                    'students':z2,
                    'postid':z3
                }
            else:
                k2=td.objects.filter(student=request.session['userid']).values()
                for k in k2.values():
                    del k['addflag']
                    del k['id']
                    z.append(k)
                for i in z:
                    l3=bio.objects.filter(userid=i['staff']).values()
                    for j in l3.values():
                        del j['mobile']
                        del j['acctype']
                        del j['designation']
                        z1.append(j)
                    for m in z1:
                        l7=td.objects.filter(staff=m['userid']).values()
                        for n in l7.values():
                            z2.append(n['student'])


                z3.append(request.session['p'])
                z4={
                    'tutor':z1,
                    'students':z2,
                    'postid':z3
                }
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':z4})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))

@csrf_exempt
def privatepost_save_ward(request):#t48
    wholeid=request.POST.getlist('wholeid[]')
    postid=request.POST.get('postid')
    data=request.POST.get('')
    if(data!='' and data!=None):
        #wholeid=data.split(',')
        pass
    uid=(request.POST.getlist('userid[]'))
    #print('postid:  ',postid)
    #print(wholeid)
    for i in wholeid:
        b=privatepost(userid=i,postid=postid)
        b.save()
    return HttpResponse('success')
def data(request):
    #now=datetime.datetime.now()
    #startdate=now-datetime.timedelta(days=7)
   #startdate=str(startdate.strftime("%d/%m/%y" ))
    #enddate=str(now.strftime("%d/%m/%y"))

    startdate="2021-05-31"
    enddate="2021-06-09"
    postdata=[]
    reqpost=[]
    gp=posts.objects.all().values()
    gp1=gp.values()
    for i in gp1:
        temp=(i['posttime'][0:8])
        i.update({'posttime':temp})
        #print(i['posttime'])
    datas=pd.DataFrame.from_dict(gp1)
    #print(datas)
    datas['posttime'] = pd.to_datetime(datas['posttime'], format='%d/%m/%y')
    filtered_df = datas.loc[(datas['posttime'] >= startdate)
                     & (datas['posttime'] <=enddate)]
    filtered_df['posttime']=filtered_df['posttime'].astype(str)
    finaldata=filtered_df.to_dict()
    #print(finaldata)




    context={

        'wholedata':finaldata

            }
    #print(context)
    return HttpResponse(json.dumps(context))
def certificate(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'certificate.html',{'s':s})

@csrf_exempt
def t49(request):
    a1=request.POST.get('rno')
    a2=request.POST.get('sd')
    a3=request.POST.get('ed')
    a4=request.POST.get('type')
    a5=request.POST.get('event_1')
    a6=request.POST.get('ndays')
    a7=request.POST.get('eloc')
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(a7)
    a8=bio.objects.filter(userid=request.session['userid']).values()
    for i in a8.values():
        a9=i['name']
    print(a9)
    a10=certificate_details(_userid=request.session['userid'],name=a9,regno=a1,startdate=a2,enddate=a3,eventtype=a4,eventname=a5
    ,eventdays=a6,location=a7)
    a10.save()
    print('saved')
    return HttpResponse("success")
def t50(request):
    check=request.GET.get('check')
    name=[]
    dp=[]
    type_1=[]
    ids=[]

    if(check=='1'):
        data=bio.objects.all().values()
        for d in data.values():
            ids.append(d['userid'])
            name.append(d['name'])
            dp.append(d['profilepic'])
            type_1.append(1)
        data1=group.objects.all().values()
        for dat in data1.values():
            ids.append(dat['groupid'])
            name.append(dat['groupname'])
            dp.append(dat['groupdp'])
            type_1.append(0)

    else:
        pass
    context={
        'id':ids,
        'name':name,
        'dp':dp,
        'type':type_1
        }
    print(context)

    return HttpResponse(json.dumps(context))

def loadcomment(request):
    check=request.GET.get('check')
    postid=request.GET.get('postid')
    postid=int(postid)
    commentdata=[]
    grpdata=[]
    if check=='1':
        for i in request.session['final']:
            if(i['postid']==postid):
                i.update({'commentstatus':1})
                grp=posts.objects.filter(postid=postid).values()
                for j in grp.values():
                    g1=group.objects.filter(groupid=j['groupid']).values()
                    for k in g1.values():
                        del k['groupid']
                        del k['adminid']
                        i.update({'groupname':k['groupname']})
                        i.update({'groupdp':k['groupdp']})
                name=bio.objects.filter(userid=i['userid']).values()
                for l in name.values():
                    i.update({'name':l['name']})
                commentdata.append(i)



    return HttpResponse(json.dumps(commentdata))

def loadtut(request):
    check=request.GET.get('check')
    userid=request.GET.get('userid')
    userid=int(userid)
    b10=td.objects.filter(student=userid).values()
    #print('mmmmmmmmmmmmmm',len(b10))
    if len(b10)!=0:
        b8=td.objects.filter(student=userid).values()
        for j in b8.values():
            del j['student']
            del j['addflag']
        tutorid=j['staff']
    else:
        tutorid='NaN--:)'
    return HttpResponse(json.dumps(tutorid))



def namelist(request):
    y=[]
    z=[]
    z1=[]
    z2=[]
    z3=[]
    target=request.GET.get('target')
    userid_1=request.GET.get('userid')
    if(userid_1!='' and userid_1!=None):
        request.session['userid']=int(userid_1)

    if target=='1':
        l1=bio.objects.filter(userid=request.session['userid']).values()
        for l in l1.values():
            if(l['acctype']==0):
                k2=td.objects.filter(staff=request.session['userid']).values()
                for k in k2.values():
                    del k['addflag']
                    del k['id']
                    z.append(k)
                for i in z:
                    l3=bio.objects.filter(userid=i['student']).values()
                    for j in l3.values():
                        del j['mobile']
                        del j['acctype']
                        del j['designation']
                        z1.append(j)

                z2.append(request.session['userid'])
                z4={
                    'z1':z1,
                    'z2':z2,

                }
            else:
                k2=td.objects.filter(student=request.session['userid']).values()
                for k in k2.values():
                    del k['addflag']
                    del k['id']
                    z.append(k)
                for i in z:
                    l3=bio.objects.filter(userid=i['staff']).values()
                    for j in l3.values():
                        del j['mobile']
                        del j['acctype']
                        del j['designation']
                        z1.append(j)
                    for m in z1:
                        l7=td.objects.filter(staff=m['userid']).values()
                        for n in l7.values():
                            z2.append(n['student'])



                z4={
                    'z1':z1,
                    'z2':z2,

                }
        return HttpResponse(json.dumps(z4))
def get_single_post(request):
    userid=request.headers['X-User']
    postid=int(request.GET.get('postid'))
    post={}
    groupdet={}
    user={}
    finaldict1={}
    '''p=posts.objects.filter(postid=postid).values()
    for data in p.values():
        gp=group.objects.filter(groupid=data['groupid']).values()
        for data1 in gp.values():'''
    for data in request.session['m11']:
        if(data['postid']==postid):
            post=data
            userd=bio.objects.filter(userid=data["userid"]).values()
            for data1 in userd.values():
                del data1['userid']
                del data1['mobile']
                del data1['acctype']
                del data1['designation']
                del data1['batch_start']
                del data1['batch_end']
                user=data1
            gpd=group.objects.filter(groupid=data['groupid']).values()
            for data2 in gpd.values():
                del data2['adminid']
                groupdet=data2
    context={
            'post':post,
            'user':user,
            'group':groupdet
        }
    finaldict1.update({'status':7})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':context})
    return HttpResponse(json.dumps(finaldict1))

"""
culturals request part

init home pending

edit profile pending

dp update pending


"""
@csrf_exempt
def event_save(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    event_name=request.POST.get('eventname')
    etype=request.POST.get('eventtype')
    a=request.POST.get('imgdata')
    desc=request.POST.get('desc')
    participants=request.POST.get('ppt')
    eventdate=request.POST.get('eventdate')
    posterpic=request.POST.get('posterpic')
    u5=userid.objects.filter(userid=useid).values()
    for data in u5.values():
        if(data['webtoken']==token or data['androidtoken']==token):
            b=a[a.find(",")+1:]
            image_64_decode = base64.b64decode(b)
            c=r'/home/mctea/machuraz/static/events/'+str(event_name)+r'.jpg'
            d=c[20:]
            image_result = open(c, 'wb+') # create a writable image and write the decoding result
            image_result.write(image_64_decode)
            b1=posterpic[posterpic.find(",")+1:]
            image_64_decode = base64.b64decode(b1)
            e=r'/home/mctea/machuraz/static/events/'+str(event_name)+'_poster'+r'.jpg'
            f=e[20:]
            image_result = open(e, 'wb+') # create a writable image and write the decoding result
            image_result.write(image_64_decode)
            b3=Events(eventname=event_name,eventpic=d,description=desc,participants_per_team=participants,posterpic=f,eventdate=eventdate,eventtype=etype)
            b3.save()
            print("event added")
            finaldict1.update({'status':'success'})
            finaldict1.update({'message':'success'})
            finaldict1.update({'data':{}})
            return HttpResponse(json.dumps(finaldict1))
        else:
            finaldict1.update({'status':'error'})
            finaldict1.update({'message':'token verification failed'})
            finaldict1.update({'data':{}})
            return HttpResponse(json.dumps(finaldict1))

@csrf_exempt
def culturals_post_save(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    post_data=request.POST.get('postdata')
    event_id=request.POST.get('eventid')
    a=request.POST.get('imgdata')
    if(check(useid,token)):
        #print(a)
        li=[]
        data1 = datetime.datetime.now()
        t=data1.strftime("%d/%m/%y %H:%M:%S")
        if(post_data=='' and a==None):
            return HttpResponse('failed')
        else:
            if a==None or a=='':
                c=''
                b2=EventUpdate(userid=useid,eventid=event_id,imgdata=c,eventmessage=post_data,postedon=t)
                b2.save()
                print("post added")
                finaldict1.update({'status':'success'})
                finaldict1.update({'message':'success'})
                finaldict1.update({'data':{}})
                return HttpResponse(json.dumps(finaldict1))
            else:

                n1=8
                res=''.join(random.choices(string.ascii_uppercase+string.digits,k=n1))
                c=r'/home/mctea/machuraz/static/posts/'+str(event_id)+'_'+str(res)+r'.jpg'
                d=c[20:]
                z=EventUpdate.objects.all().values()
                if len(z)==0:
                    b=a[a.find(",")+1:]
                    image_64_decode = base64.b64decode(b)
                    image_result = open(c, 'wb+') # create a writable image and write the decoding result
                    image_result.write(image_64_decode)
                    print('imagesaved')
                else:
                    for i in z.values():
                        del i['eventid']
                        del i['userid']
                        del i['eventmessage']
                        del i['postedon']
                        li.append(i)
                    print(li)
                    for i in li:
                        if i['imgdata']==c:
                            res=''.join(random.choices(string.ascii_uppercase+string.digits,k=n1))
                            c=r'/home/mctea/machuraz/static/posts/'+str(event_id)+'_'+str(res)+r'.jpg'
                            d=c[20:]
                        else:
                            b=a[a.find(",")+1:]
                            image_64_decode = base64.b64decode(b)
                            image_result = open(c, 'wb+') # create a writable image and write the decoding result
                            image_result.write(image_64_decode)
                            print('imagesaved')
                b4=EventUpdate(userid=useid,eventid=event_id,imgdata=d,eventmessage=post_data,postedon=t)
                b4.save()
                print("post added")
                finaldict1.update({'status':'success'})
                finaldict1.update({'message':'success'})
                finaldict1.update({'data':{}})
                return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))

@csrf_exempt
def init_events(request):
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    eventid=request.POST.get('eventid')
    finaldict1={}
    tempdict={}
    tempdict1={}
    querydict={}
    queries=[]
    u5=userid.objects.filter(userid=useid).values()
    for data1 in u5.values():
        if(data1['webtoken']==token or data1['androidtoken']==token):
            e1=Events.objects.filter(eventid=eventid).values()
            for data in e1.values():
                eventid=data['eventid']
                eventname=data['eventname']
                eventpic=data['eventpic']
                desc=data['description']
                participants=data['participants_per_team']
                poster=data['posterpic']
                eventdate=data['eventdate']
                e3=Registration.objects.filter(eventid=data['eventid']).filter(userid=useid).values()
                if(len(e3)==0):
                     tempdict1.update({'regnStatus':0})
                else:
                    for data in e3.values():
                        tempdict1.update({'regnStatus':1})
                tempdict1.update({'eventId':eventid})
                tempdict1.update({'eventname':eventname})
                tempdict1.update({'description':desc})
                tempdict1.update({'img':eventpic})
                tempdict1.update({'participants_per_team':participants})
                tempdict1.update({'posterpic':poster})
                tempdict1.update({'eventdate':eventdate})
            e4=Registration.objects.filter(eventid=eventid).values()
            tempdict1.update({'participants_count':len(e4)})
            tempdict.update({'eventDetails':tempdict1})
            e2=EventQueries.objects.filter(eventid=eventid).values()
            for data in e2.values():
                querydict.update({'queryid':data['id']})
                c1=data['query'].encode('ascii').decode('unicode-escape').encode('utf-16', 'surrogatepass').decode('utf-16')
                querydict.update({'query':c1})
                querydict.update({'postedby':data['postedby']})
                querydict.update({'respondedby':data['respondedby']})
                if(data['response']!=None and data['response']!=""):
                    c2=data['response'].encode('ascii').decode('unicode-escape').encode('utf-16', 'surrogatepass').decode('utf-16')
                    querydict.update({'response':c2})
                else:
                    querydict.update({'response':data['response']})
                queries.append(querydict)
                querydict={}
            tempdict.update({'queries':queries})


            finaldict1.update({'status':'success'})
            finaldict1.update({'message':'1-success'})
            finaldict1.update({'data':tempdict})
            return HttpResponse(json.dumps(finaldict1))
        else:
            finaldict1.update({'status':'error'})
            finaldict1.update({'message':'token verification failed'})
            finaldict1.update({'data':{}})
            return HttpResponse(json.dumps(finaldict1))

@csrf_exempt
def init_queries(request):
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    eventid=request.POST.get('eventid')
    finaldict1={}
    tempdict={}
    tempdict1={}
    querydict={}
    queries=[]
    if(check(useid,token)):
        e1=Events.objects.filter(eventid=eventid).values()
        for data in e1.values():
            eventid=data['eventid']
            eventname=data['eventname']
            poster=data['posterpic']
            tempdict1.update({'eventId':eventid})
            tempdict1.update({'eventname':eventname})
            tempdict1.update({'posterpic':poster})
            tempdict.update({'eventDetails':tempdict1})
        e2=EventQueries.objects.filter(eventid=eventid).values()
        for data in e2.values():
            querydict.update({'queryid':data['id']})
            c1=data['query'].encode('ascii').decode('unicode-escape').encode('utf-16', 'surrogatepass').decode('utf-16')
            querydict.update({'query':c1})
            querydict.update({'postedby':data['postedby']})
            querydict.update({'respondedby':data['respondedby']})
            if(data['response']!=None and data['response']!=""):
                c2=data['response'].encode('ascii').decode('unicode-escape').encode('utf-16', 'surrogatepass').decode('utf-16')
                querydict.update({'response':c2})
            else:
                querydict.update({'response':data['response']})
            queries.append(querydict)
            querydict={}
        tempdict.update({'queries':queries})
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'2-success'})
        finaldict1.update({'data':tempdict})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
@csrf_exempt
def raise_query(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    query1=request.POST.get('query')
    query_text=query1.encode('unicode-escape').decode('ASCII')
    eventid=request.POST.get('eventid')
    if(check(useid,token)):
        e1=EventQueries.objects.create(eventid=eventid,query=query_text,postedby=useid)
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
@csrf_exempt
def respond_query(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    query1=request.POST.get('query')
    query_response=query1.encode('unicode-escape').decode('ASCII')
    queryid=request.POST.get('queryid')
    if(check(useid,token)):
        e1=EventQueries.objects.filter(id=queryid).update(respondedby=useid,response=query_response)
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
@csrf_exempt
def register_event(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    eventid=request.POST.get('eventid')
    if(check(useid,token)):
        e1=Registration(eventid=eventid,userid=useid)
        e1.save()
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))

@csrf_exempt
def delete_query(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    queryid=request.POST.get('queryId')
    if(check(useid,token)):
        e1=EventQueries.objects.filter(id=queryid).delete()
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
@csrf_exempt
def unregister(request):
    finaldict1={}
    useid=request.headers['X-User']
    token=request.headers['X-Token']
    eventid=request.POST.get('eventid')
    if(check(useid,token)):
        e1=Registration.objects.filter(userid=useid).filter(eventid=eventid).delete()
        finaldict1.update({'status':'success'})
        finaldict1.update({'message':'success'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
    else:
        finaldict1.update({'status':'error'})
        finaldict1.update({'message':'token verification failed'})
        finaldict1.update({'data':{}})
        return HttpResponse(json.dumps(finaldict1))
@csrf_exempt
def excel_filter(request):
    finaldict1={}
    eventid=request.POST.get('eventid')
    datas=[]
    temp={}
    e1=Registration.objects.filter(eventid=eventid).values()
    for data in e1:
        eve=data['eventid']
        use=data['userid']
        m1=bio.objects.filter(userid=use).values()
        for i in m1.values():
            name=i['name']
            reg_no=i['reg_no']
            mobile=i['mobile']
            temp.update({"Name":name,"reg_no":reg_no,"mobile":mobile})
        m3=userid.objects.filter(userid=use).values()
        for k in m3.values():
            mail=k['email']
            temp.update({"Email":mail})
        m2=Events.objects.filter(eventid=eve).values()
        print("/////////////")
        print(m2)
        for j in m2:
            eventname=j['eventname']
            temp.update({"event":j['eventname']})
        datas.append(temp)
        print(datas)
        print("dict appended")
        df = pd.DataFrame.from_dict(datas)
        temp={}
        print(temp)
    date1 = datetime.datetime.now()
    t=date1.strftime("%d_%m_%y_%H-%M-%S")
    print(t)
    p=r'/home/mctea/machuraz/static/excel/'+eventname+"_"+str(t)+r'_registered.xlsx'
    fp=p[21:]
    df.to_excel(p,index=False)
    finaldict1.update({'status':'success'})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':r'https://mectmoment.pythonanywhere.com/'+str(fp)})
    return HttpResponse(json.dumps(finaldict1))
@csrf_exempt
def participants_filter(request):
    finaldict1={}
    eventid=request.POST.get('eventid')
    datas=[]
    temp={}
    e1=Registration.objects.filter(eventid=eventid).values()
    for data in e1:
        eve=data['eventid']
        use=data['userid']
        m1=bio.objects.filter(userid=use).values()
        for i in m1.values():
            name=i['name']
            reg_no=i['reg_no']
            temp.update({"Name":name,"reg_no":reg_no})
            datas.append(temp)
            temp={}
    finaldict1.update({'status':'success'})
    finaldict1.update({'message':'success'})
    finaldict1.update({'data':datas})
    return HttpResponse(json.dumps(finaldict1))
def db_thankyou(request):
    m1=Events.objects.all().delete()
    m2=EventUpdate.objects.all().delete()
    m3=Registration.objects.all().delete()
    m4=EventQueries.objects.all().delete()
    return HttpResponse('<center>Thank you have a nice day</center>')
@csrf_exempt
def logout(request):
    req=request.POST.get('logout')
    finaldict1={}
    userid_1=request.headers['X-User']
    token=request.headers['X-Token']
    tokencheck=request.POST.get('isweb')
    if(req=='1'):
        #apikey="AAAA-_B-JEI:APA91bGTzkC8n_fsX0NuoQY5p7xY4iDzhOXmmKuX1Fr6Mtwbnl3CZNPle-8S17Bs-v3leYrjMesUl4Xy8FdZVVsYkHQI5k-6Dspd1XtUVtfwiliNTiXQu4EuAAp6_bYK0BY6oCl0OLND"
        tokens=[]
        if(check(userid_1,token)):
            fdata=fcmdata.objects.filter(userid=userid_1).values()
            #print(fdata[0]['fcmtoken'])
            tokens.append(fdata[0]['fcmtoken'])
            p#rint(tokens)
            for data in fdata.values():
                print(data['topics_subscribed'],"................")
                if(data['topics_subscribed']=='MECT-General'):
                    if(topicunsubscription(apikey,tokens,data['topics_subscribed'])==1):
                        print("Unsubscribed: ",data['topics_subscribed'])
                    else:
                        print("Error in unsubscribption: ",data['topics_subscribed'])

                        return HttpResponse('0')

            if(tokencheck=='1'):
                u1=userid.objects.filter(userid=userid_1).update(webtoken="NaN--:)")
            else:
                u1=userid.objects.filter(userid=userid_1).update(androidtoken="NaN--:)")
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    else:

        return HttpResponse('0')

def notify(topic,messagetitle,messagebody):
    result = push_service.notify_topic_subscribers(topic_name=topic,message_title=messagetitle, message_body=messagebody,click_action="FLUTTER_NOTIFICATION_CLICK",color="red")
    print(result)
    print("Notiication triggered for topic: ",topic)
    return 1
def notifybatch(ids,message_title,message_body):
    print('testing fcm...', ids, message_title, message_body)
    result = push_service.notify_multiple_devices(registration_ids=ids, message_title=message_title, message_body=message_body)
    print(result)
    print("Notification triggered for specific people")
    return 1




















