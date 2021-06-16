from.models import userid,bio,group,followers_group,posts,privatepost,like,privatereply,comment,followers_people,darkmode,notificationcount,ntime,logout,td,studentdetails,certificate_details
from django.shortcuts import render,redirect,HttpResponse
from passlib.hash import pbkdf2_sha256
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

# Create your views here.

def t1(request):
    global email
    email=(request.POST.get('email'))
    password=request.POST.get('pwd')
    req=request.POST.get('request')
    enc=pbkdf2_sha256.hash(str(password))
    a1=userid.objects.filter(email=email).values()
    if req=='1':
        try:
            a=userid(email=email,password=enc)
            a.save()
            return HttpResponse(json.dumps('success'))

        except :
            print('ierror')
            return HttpResponse(json.dumps('email exists'))
    else:
        pass


def t2(request):
    a=request.GET.get('request1')
    if a=='1':
        data=email
        return HttpResponse(data)
    else:
        pass
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



def t4(request):

    req2=request.POST.get('request2')
    a=request.POST.get('imgdata')
    userid_1=request.POST.get('userid')
    userid_1=int(userid_1)
    if(userid_1!='' and userid_1!=None):
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
def t30(request):
    userid_1=request.POST.get('userid')
    userid_1=int(userid_1)
    if(userid_1!='' and userid_1!=None):
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
    if(i23==''or i23==Noneandi==None):
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
def t5(request):
    login=request.POST.get('login')
    mail=request.POST.get('email')
    password=request.POST.get('password')
    g=userid.objects.all().values()
    for i in g.values():
        j=i['email']
        if j==mail:
            k=userid.objects.filter(email=mail).values()
            for j in k:
                l=j['password']
                id1=j['userid']
                request.session['userid']=id1
                enc=pbkdf2_sha256.verify(password,l)
                if enc==True:
                    print('password true')
                    l10=logout.objects.filter(userid=request.session['userid']).update(lflag=0)
                    return HttpResponse('Success')
                else:
                    print('password incorrect')
                    return HttpResponse('failed')
    else:
        return HttpResponse('email failed')

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

def t7(request):
    search=request.POST.get('search')
    name=request.POST.get('name')
    s1=bio.objects.filter(name__istartswith=name).values()
    s2=group.objects.filter(groupname__istartswith=name).values()
    bd=[]
    gd=[]
    l=[]
    for i in s1.values():
        del i['mobile']
        del i['acctype']
        del i['designation']
        bd.append(i)


    for j in s2:
        del j['adminid']
        gd.append(j)
    l=bd+gd
    print(l)
    return HttpResponse(json.dumps(l))
def t8(request):
    type1=request.POST.get('type1')
    searchid=request.POST.get('id')
    request.session['searchid']=searchid
    print(type1)
    return HttpResponse('success')
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
def t10(request):
    pdata=request.GET.get('postdata')
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
        return HttpResponse(json.dumps(g))
    else:
        return HttpResponse("pdata value is not 1")

def t11(request):
    li=[]
    posttext=request.POST.get('posttext')
    print('inposttext'+posttext)
    a=request.POST.get('postimg')
    print
    useid=request.POST.get('userid')
    request.session['useid']=useid
    groupname=request.POST.get('groupname')
    n1=8
    res=''.join(random.choices(string.ascii_uppercase+string.digits,k=n1))
    if posttext=='' and a==None:
        print('no')
        return HttpResponse('no')
    else:
        if a==None or a=='':
            c='NULL'
        else:
            b=a[a.find(",")+1:]
            image_64_decode = base64.b64decode(b)
            c=r'static/post/'+r'post_'+str(request.session['useid'])+'_'+str(res)+r'.jpg'
            z=posts.objects.all().values()
            if len(z)==0:
                image_result = open(c, 'wb+') # create a writable image and write the decoding result
                image_result.write(image_64_decode)
                print('imagesaved')
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
                    if i['imgdata']==c:
                        res=''.join(random.choices(string.ascii_uppercase+string.digits,k=n1))
                        c=r'static/post/'+r'post_'+str(request.session['useid'])+'_'+str(res)+r'.jpg'
           
                    else:
                        image_result = open(c, 'wb+') # create a writable image and write the decoding result
                        image_result.write(image_64_decode)
                        print('imagesaved')
        print(posttext)
        print(groupname)
        now=datetime.datetime.now()
        t=now.strftime("%d/%m/%y %H:%M:%S")
        print(t)
        k=group.objects.filter(groupname=groupname).values()
        print(k)
        for i in k.values():
            j=i['groupid']
        #print(j)
        b2=posts(userid=request.session['useid'],groupid=j,postdata=posttext,imgdata=c,posttime=t)
        b2.save()
        print('saved in db')
        k1=posts.objects.filter(userid=request.session['useid']).values()
        for i in k1.values():
            p=i['postid']
            request.session['p']=p
            u=i['groupid']
            request.session['u']=u
        return HttpResponse(json.dumps(p))
def t12(request):

    y=[]
    z=[]
    z1=[]
    z2=[]
    target=request.GET.get('target')
    userid_1=request.GET.get('userid')
    print('t12 userid',userid_1)
    postid=request.GET.get('postid')
    if(userid_1!='' and userid_1!=None):
        request.session['userid']=int(userid_1)
    if(postid!='' and postid!=None):
        request.session['p']=int(postid)

    if target=='1':
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
                'z1':z1,
                'z2':z2
                }

        return HttpResponse(json.dumps(z3))

    else:
        pass
def t13(request):
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
def t16(request):
    postrequest=request.GET.get('postrequest')
    if postrequest=='1':

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
            i.update({'commentdata':'null'})
            i.update({'commenttime':'null'})
            i.update({'commentstatus':0})
            i.update({'dp':'null'})
            i.update({'delete':0})
            request.session['m10'].append(i)
        request.session['m10'].reverse()
        print(p1)
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
                    #print('postid diffErent')
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
            i.update({'dp':'null'})
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
        request.session['final']=request.session['m10'].copy()
        print(request.session['m11'])
        z1=len(request.session['m11'])
        for i in request.session['m11']:
            if i['userid']==request.session['userid']:
                i['delete']=1
            else:
                pass

        print(z1)


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

        context={
            'post':s,
            'user':x,
            'group':y,
            'userdp':request.session['n12'],
            'username':request.session['n13'],
            'length':z1

        }

        return HttpResponse(json.dumps(context))
    else:
        pass
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
            i.update({'commentdata':'null'})
            i.update({'commenttime':'null'})
            i.update({'commentstatus':0})
            i.update({'dp':'null'})

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
            i.update({'dp':'null'})
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
def t17(request):
    c=request.GET.get('startpost')
    a=request.GET.get('endpost')
    print('----------------------------------------')
    print(c)
    print(a)
    print('----------------------------------------')
    b=[]
    e=[]
    d=[]
    for i in request.session['m11'][int(c):int(a)]:
        b.append(i)
    for i in request.session['a10'][int(c):int(a)]:
        e.append(i)
    for i in request.session['b10'][int(c):int(a)]:
        d.append(i)
    context={
            'post':b,
            'user':e,
            'group':d
        }
    print(context)

    return HttpResponse(json.dumps(context))
def t18(request):
    j=[]
    k=[]
    postid=request.POST.get('postid')
    likestatus=request.POST.get('likestatus')
    print(postid)
    print(likestatus)
    now=datetime.datetime.now()
    t=now.strftime("%d/%m/%y %H:%M:%S")
    print(t)
    if likestatus=='1':
        l3=like.objects.filter(postid=postid).all().values()
        for i in l3.values():
            del i['id']
            j.append(i)
        print(j)
        if len(j)==0:
            l5=like(postid=postid,userid=request.session['userid'],liketime=t)
            l5.save()
            print('len saved')
        else:
            for i in j:
                print(i['postid'])
                print(int(postid))
                print(i['userid'])
                print(request.session['userid'])
                if (i['postid']==int(postid)) and (i['userid']==request.session['userid']):
                    print('same pu')
                    pass
                else:
                    l5=like(postid=postid,userid=request.session['userid'],liketime=t)
                    l5.save()
                    print('else saved')
                    break
    else:
        l6=like.objects.filter(postid=postid).filter(userid=request.session['userid']).delete()
    l4=like.objects.filter(postid=postid).all().values()
    for i in l4.values():
       k.append(i['postid'])
    print(k)
    x=len(k)
    print('count',x)
    p2=posts.objects.filter(postid=postid).values()
    for i in p2.values():
        p1id=i['postid']
        u1id=i['userid']
        gp1id=i['groupid']
        pd1=i['postdata']
        img1=i['imgdata']
        pttime=i['posttime']
    p3=posts(postid=p1id,userid=u1id,groupid=gp1id,postdata=pd1,imgdata=img1,posttime=pttime,likecount=x)
    p3.save()
    return HttpResponse('sucess')

def t19(request):
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
        img1=i['imgdata']
        pttime=i['posttime']
    p3=posts(postid=p1id,userid=u1id,groupid=gp1id,postdata=pd1,imgdata=img1,posttime=pttime,likecount=x)
    p3.save()
    return HttpResponse('sucess')
def t20(request):
    now=datetime.datetime.now()
    t=now.strftime("%d/%m/%y %H:%M:%S")
    idto=request.POST.get('reply_to')
    postid=request.POST.get('post_id')
    replydata=request.POST.get('replydata')
    r=privatereply(idfrom=request.session['userid'],idto=idto,replydata=replydata,replytime=t,postid=postid)
    r.save()
    return HttpResponse('success')
def t21(request):
    now=datetime.datetime.now()
    t=now.strftime("%d/%m/%y %H:%M:%S")
    postid=request.POST.get('post_id')
    commentdata=request.POST.get('commentdata')
    c=comment(postid=postid,userid=request.session['userid'],commentdata=commentdata,commenttime=t)
    c.save()
    return HttpResponse('success')
def t24(request):
    gdata=request.GET.get('getgroupdata')
    fgrpid=request.GET.get('gid1')
    print('******************',fgrpid)
    if(fgrpid==None):
        pass
    else:
        request.session['gid1']=int(fgrpid)
        print('******************',fgrpid)
        print( 'in else t24-----',request.session['gid1'])


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
    print('/////',request.session['w'])
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
                del j['groupid']
                request.session['x2'].append(j)

    z2=len(request.session['w'])
    for i in request.session['w'][0:10]:
        x3.append(i)
    for i in request.session['x1'][0:10]:
        x4.append(i)
    for i in request.session['x2'][0:10]:
        x5.append(i)
    print(z2)
    context={
            'post':x3,
            'user':x4,
            'group':x5,
            'userdp':request.session['n12'],
            'length':z2
        }
    print(context)

    return HttpResponse(json.dumps(context))
def t25(request):
    c=request.GET.get('startpost')
    a=request.GET.get('endpost')
    print(c)
    print(a)
    b=[]
    e=[]
    d=[]
    for i in request.session['w'][int(c):int(a)]:
        b.append(i)
    for i in request.session['x1'][int(c):int(a)]:
        e.append(i)
    for i in request.session['x2'][int(c):int(a)]:
        d.append(i)
    context={
            'post':b,
            'user':e,
            'group':d
        }


    return HttpResponse(json.dumps(context))
def t26(request):
    rinfo=request.GET.get('requestinfo')
    x3=[]
    fgrpid=request.GET.get('gid1')
    print('******************',fgrpid)
    if(fgrpid==None):
        pass
    else:
        request.session['gid1']=int(fgrpid)
        print('******************',fgrpid)
        print( 'in else t24-----',request.session['gid1'])

    print(request.session['gid1'])
    if rinfo=='1':
        g15=group.objects.filter(groupid=request.session['gid1']).values()
        for j in g15.values():
            del j['adminid']
            del j['groupid']
            x3.append(j)
            break
        print(x3)
        return HttpResponse(json.dumps(x3))
    else:
        print("ele")
        pass
def t27(request):
    lout=request.GET.get('logout')
    if lout=='1':
        d9=logout.objects.filter(userid=request.session['userid']).update(lflag=1)
        print('success flag changed')
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
    print(request.session['dark'])
    d2=darkmode.objects.filter(userid=request.session['userid']).update(dark=request.session['dark'])
    return HttpResponse('success')
def t32(request):
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
def t34(request):
    nt=request.GET.get('notificationtime')

    if nt=='1':
        now=datetime.datetime.now()
        t=now.strftime("%d/%m/%y %H:%M:%S")
        print(t)
        n3=notificationcount.objects.filter(userid=request.session['userid']).values()
        for i in n3.values():
            if i['nocount']==1:
                n4=ntime.objects.filter(userid=request.session['userid']).update(ptime=t)
                n5=ntime.objects.filter(userid=request.session['userid']).update(etime=t)
                print('in n5')
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
                            print(a2)
                            a2=[i for i in a2 if not (i['userid']==request.session['userid'])]
                            print(a2)
                        else:
                            pass
                j6=sorted(a2,key=lambda i: (i['commenttime']),reverse=True)

                a3=[]
                r9=like.objects.all().values()
                for i in r9.values():
                    i.update({'type':'like'})
                    r11=bio.objects.filter(userid=i['userid']).values()
                    for l in r11.values():
                        i.update({'userid':l['userid']})
                        i.update({'name':l['name']})
                        i.update({'dp':l['profilepic']})
                    r10=posts.objects.filter(postid=i['postid']).values()
                    for j in r10.values():
                        if j['userid']==request.session['userid']:
                            r12=group.objects.filter(groupid=j['groupid']).values()
                            for k in r12.values():
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
                a5=[]
                a5=a6+a7+j6
                #print(a5)
                j9=sorted(a5,key=lambda i: (i['commenttime']),reverse=True)
                context={
                    'latest':j9
                }
                return HttpResponse(json.dumps(context))
            else:
                now=datetime.datetime.now()
                t=now.strftime("%d/%m/%y %H:%M:%S")
                n5=ntime.objects.filter(userid=request.session['userid']).values()
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
                    i.update({'type':'comment'})
                    r8=bio.objects.filter(userid=i['userid']).values()
                    for l in r8.values():
                        i.update({'userid':l['userid']})
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
                            a2=[i for i in a2 if not (i['userid']==request.session['userid'])]
                        else:
                            pass
                j6=sorted(a2,key=lambda i: (i['commenttime']),reverse=True)

                a3=[]
                r9=like.objects.all().values()
                for i in r9.values():
                    i.update({'type':'like'})
                    r11=bio.objects.filter(userid=i['userid']).values()
                    for l in r11.values():
                        i.update({'userid':l['userid']})
                        i.update({'name':l['name']})
                        i.update({'dp':l['profilepic']})
                    r10=posts.objects.filter(postid=i['postid']).values()
                    for j in r10.values():
                        if j['userid']==request.session['userid']:
                            r12=group.objects.filter(groupid=j['groupid']).values()
                            for k in r12.values():
                                i.update({'gname':k['groupname']})
                            del i['postid']
                            a3.append(i)
                            print(a3)
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
                a5=[]
                a5=a6+a7+j6
                #print(a5)
                j9=sorted(a5,key=lambda i: (i['commenttime']),reverse=True)
                print(j9)

                latest=[]
                earlier=[]
                n10=ntime.objects.filter(userid=request.session['userid']).values()
                for j in n10.values():
                    for i in j9:
                        if i['commenttime']>j['ptime'] and i['commenttime']<j['etime'] :
                            latest.append(i)
                        else:
                            earlier.append(i)
                earlier.reverse()

                context={
                    'latest':latest,
                    'earlier':earlier,
                    'n10':j9
                }
                return HttpResponse(json.dumps(context))

    else:
        pass
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
def t36(request):
    req=request.GET.get('request')
    did=request.GET.get('nofid')
    type_1=request.GET.get('type')
    userid=request.GET.get('userid')
    if(did!=''and did!=None and type_1!='' and type_1!=None and userid!='' and userid!=None):
        request.session['did']=int(did)
        request.session['typ']=type_1
        request.session['userid']=int(userid)
        print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\',request.session['userid'])
    else:
        pass
    if req=='1':
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
                        print(j['userid'])
                        print('in or',j['likestatus'])
                        print('------------------------',i['postid'],j['postid'],'---------------------------------------------',j['userid'],';;;',request.session['userid'],type(j['userid']),';;;',type(request.session['userid']))

                        if i['postid']==j['postid'] and j['userid']==request.session['userid']:
                            i.update({'likestatus':j['likestatus']})
                            i.update({'delete':j['delete']})
                            i.update({'commentstatus':0})

                        else:
                            pass
                print('in x1',x1)

            z5=[]
            z10=bio.objects.filter(userid=request.session['userid']).values()
            for i in z10.values():
                z5.append(i['profilepic'])
            context={
                'pdata':x1,
                'cdata':x2,
                'logindp':z5,
                'dummy':request.session['final']
            }
            return HttpResponse(json.dumps(context))
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
            print('****************************************************************************')
            print(y1)
            y4=[]
            y4=y2+y3
            print(y4)
            for i in y1:
                for j in request.session['m11']:
                    print('------------------------',i['postid'],j['postid'],'---------------------------------------------',j['userid'],';;;',request.session['userid'])
                    if i['postid']==j['postid'] and j['userid']==request.session['userid']:
                        i.update({'likestatus':j['likestatus']})
                        i.update({'delete':j['delete']})
                        i.update({'commentstatus':1})
                    else:
                        pass
            print(y1)
            z5=[]
            z10=bio.objects.filter(userid=request.session['userid']).values()
            for i in z10.values():
                z5.append(i['profilepic'])
            context={
                'pdata':y1,
                'cdata':y4,
                'logindp':z5
            }
            return HttpResponse(json.dumps(context))
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
                    print(j['userid'])
                    if i['postid']==j['postid'] and j['userid']==request.session['userid']:
                        i.update({'likestatus':j['likestatus']})
                        i.update({'delete':j['delete']})
                    else:
                        pass
            print(z1)
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
            return HttpResponse(json.dumps(context))
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
def t41(request):
    del1=request.POST.get('deletepost')
    print(del1)

    if del1=='1':
        pid=request.POST.get('postid')
        print(pid)
        d6=posts.objects.filter(postid=pid).values()
        print(d6)
        for data in d6.values():
            deldata=data['imgdata']
        d1=posts.objects.filter(postid=pid).delete()
        d2=comment.objects.filter(postid=pid).delete()
        d3=like.objects.filter(postid=pid).delete()
        d4=privatereply.objects.filter(postid=pid).delete()
        d5=privatepost.objects.filter(postid=pid).delete()
        print("post deleted")
        if(deldata=='NULL'):
            print('datanull')
        else:
            print('not null')
            os.remove(deldata)
        return HttpResponse("post deleted")
    else:
        pass
def cpass(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'changepassword.html',{'s':s})
def t42(request):
    password=request.POST.get('currentpassword')
    userid_1=request.POST.get('userid')
    print(password)
    if(userid_1!='' and userid_1!=None):
        request.session['userid']=int(userid_1)
    pa1=userid.objects.filter(userid=request.session['userid'])
    for i in pa1.values():
        l=i['password']
        enc=pbkdf2_sha256.verify(password,l)
        if enc==True:
            print('password true')
            return HttpResponse('Success')
        else:
            return HttpResponse('Error')
def t43(request):
    password=request.POST.get('newpassword')
    print('changed password----------------',password)
    userid_1=request.POST.get('userid')
    if(userid_1!='' and userid_1!=None):
        request.session['userid']=int(userid_1)
    pw=enc=pbkdf2_sha256.hash(str(password))
    print('hashedpassword----------------',pw)
    pa1=userid.objects.filter(userid=request.session['userid']).update(password=pw)
    print('passwd updated')
    return HttpResponse('Success')
def t44(request):
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

        return HttpResponse(json.dumps(z1))
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



def t45(request):
    p2=request.POST.getlist('userid[]')
    tutid=request.POST.get('tutorid')
    if(tutid!='' and tutid!=None):
        si=int(tutid)
        n2=td(staff=si,student=request.session['userid'],addflag=1)
        n2.save()
        print('tutor added')
    else:
        if len(p2)==0:
            pass
        else:
            for i in p2:
                si=int(i)
            print(si)
            n2=td(staff=si,student=request.session['userid'],addflag=1)
            n2.save()
            print('tutor added')
    return HttpResponse('Success')
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
def t47(request):
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
                z3.append(request.session['p'])
                z2.append(request.session['userid'])
                z4={
                    'z1':z1,
                    'z2':z2,
                    'z3':z3
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
                    'z1':z1,
                    'z2':z2,
                    'z3':z3
                }
        return HttpResponse(json.dumps(z4))
def t48(request):
    wholeid=request.POST.getlist('wholeid[]')
    postid=request.POST.get('postid')
    data=request.POST.get('')
    if(data!='' and data!=None):
        #wholeid=data.split(',')
        pass
    uid=(request.POST.getlist('userid[]'))
    print('postid:  ',postid)
    print(wholeid)
    for i in wholeid:
        b=privatepost(userid=i,postid=postid)
        b.save()
    return HttpResponse('success')
def data(request):
    now=datetime.datetime.now()
    startdate=now-datetime.timedelta(days=7)
    startdate=str(startdate.strftime("%d/%m/%y" ))
    enddate=str(now.strftime("%d/%m/%y"))
    pval=posts.objects.raw('SELECT * from mectworkplace_posts where posttime>=%s AND posttime<=%s',[startdate,enddate])
    print('/././././././././././././.',pval)
    postdata=[]
    reqpost=[]
    print(startdate)
    print(pval)
    for i in pval:
        postdata.append(i)



    context={
        'startdate':startdate,
        'enddate':enddate,
        'postdata':reqpost,
        'wholedata':postdata

            }
    return HttpResponse(json.dumps(context))
def certificate(request):
    b7=darkmode.objects.filter(userid=request.session['userid'])
    for i in b7.values():
        del i['id']
        del i['userid']
    s=i['dark']
    return render(request,'certificate.html',{'s':s})
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
    print('mmmmmmmmmmmmmm',len(b10))
    if len(b10)!=0:
        b8=td.objects.filter(student=userid).values()
        for j in b8.values():
            del j['student']
            del j['addflag']
        tutorid=j['staff']
    else:
        tutorid='null'
    return HttpResponse(json.dumps(tutorid))







































