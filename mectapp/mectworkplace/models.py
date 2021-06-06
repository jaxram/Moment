from django.forms import ModelForm
from django.db import models

class userid(models.Model):
    userid=models.AutoField(primary_key=True)
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=256)




class bio(models.Model):
    userid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    mobile=models.CharField(max_length=11,unique=True)
    acctype=models.IntegerField(max_length=1)
    designation=models.IntegerField(max_length=45)
    profilepic=models.CharField(max_length=45,null=True)
    class Meta:
        indexes = [
            models.Index(fields=['userid'], name='fk_bio_id1_idx'),


        ]
class comment(models.Model):
    postid=models.IntegerField()
    userid=models.IntegerField()
    commentdata=models.CharField(max_length=200,null=True)
    commenttime=models.CharField(max_length=35,null=True)
    class Meta:
        indexes = [
            models.Index(fields=['postid'], name='fk_comment_posts1_idx'),
            models.Index(fields=['userid'], name='fk_comment_id1_id'),


        ]
class followers_group(models.Model):
    userid=models.IntegerField()
    groupid=models.IntegerField()
    class Meta:
        indexes = [
            models.Index(fields=['groupid'], name='fk_followers_group_groups1_idx'),



        ]
class followers_people(models.Model):
    id_to_follow=models.IntegerField()
    id_follow=models.IntegerField()
    class Meta:
        indexes = [
            models.Index(fields=['id_to_follow'], name='fk_followers_people_id1_idx'),
            models.Index(fields=['id_follow'], name='fk_followers_people_id2_idx'),


        ]



class joinrequest(models.Model):
    personid=models.IntegerField()
    groupd=models.IntegerField()
    class Meta:
        indexes = [
            models.Index(fields=['personid'], name='fk_joinrequest_id1_idx'),
            models.Index(fields=['groupd'], name='fk_joinrequest_groups1_idx'),


        ]
class like(models.Model):
    postid=models.IntegerField()
    userid=models.IntegerField()
    liketime=models.CharField(max_length=35,null=True)
    class Meta:

        indexes = [
            models.Index(fields=['postid'], name='fk_like_posts1_idx'),
            models.Index(fields=['userid'], name='fk_like_id1_idx'),


        ]
class posts(models.Model):
    postid=models.AutoField(primary_key=True)
    userid=models.IntegerField(null=True)
    groupid=models.IntegerField()
    postdata=models.CharField(max_length=500,null=True)
    imgdata=models.CharField(max_length=100,null=True)
    posttime=models.CharField(max_length=35,null=True)
    likecount=models.IntegerField(default=0)
    class Meta:
        indexes = [
            models.Index(fields=['groupid'], name='fk_posts_groups1_idx'),
            models.Index(fields=['userid'], name='fk_posts_id1_idx'),


        ]
class privatereply(models.Model):
    idfrom=models.IntegerField()
    idto=models.IntegerField()
    replydata=models.CharField(max_length=200)
    replytime=models.CharField(max_length=35,null=True)
    postid=models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['idfrom'], name='fk_privatereply_id1_idx'),
            models.Index(fields=['idto'], name='fk_privatereply_id2_idx'),

        ]
class privatepost(models.Model):
    userid=models.IntegerField()
    postid=models.IntegerField()
class darkmode(models.Model):
    userid=models.IntegerField(default=0)
    dark=models.IntegerField(default=0)
class notificationcount(models.Model):
    userid=models.IntegerField(default=0,unique=True)
    nocount=models.IntegerField(default=0)
class ntime(models.Model):
    userid=models.IntegerField(default=0,unique=True)
    ptime=models.CharField(max_length=50)
    etime=models.CharField(max_length=50)
class group(models.Model):
    groupid=models.AutoField(primary_key=True)
    adminid=models.IntegerField()
    groupname=models.CharField(max_length=45,unique=True)
    groupdp=models.CharField(max_length=100,null=True)
    class Meta:
        indexes = [
            models.Index(fields=['adminid'], name='fk_groups_id1_idx'),

        ]
class logout(models.Model):
    userid=models.IntegerField(default=0)
    lflag=models.IntegerField(default=0)
class td(models.Model):
    staff=models.IntegerField(default=0)
    student=models.IntegerField(default=0,unique=True)
    addflag=models.IntegerField(default=0)
class studentdetails(models.Model):
    userid=models.IntegerField(default=0,unique=True)
    name=models.CharField(max_length=50)
    rollno=models.IntegerField(default=0)
    regno=models.CharField(max_length=10)
    degree=models.CharField(max_length=50)
    degree_details=models.CharField(max_length=50)
    community=models.CharField(max_length=50,null=True)
    religion=models.CharField(max_length=50)
    blood=models.CharField(max_length=10)
    dob=models.CharField(max_length=20)
    address=models.CharField(max_length=300)
    brother=models.IntegerField(default=0)
    sister=models.IntegerField(default=0)
    father_name=models.CharField(max_length=50)
    father_mobile=models.CharField(max_length=11)
    father_mail=models.CharField(max_length=50)
    father_occupation=models.CharField(max_length=50)
    foccupation_type=models.CharField(max_length=50)
    father_income=models.IntegerField(default=0)
    mother_name=models.CharField(max_length=50)
    mother_mobile=models.CharField(max_length=11)
    mother_mail=models.CharField(max_length=50)
    mother_occupation=models.CharField(max_length=50)
    moccupation_type=models.CharField(max_length=50)
    mother_income=models.IntegerField(default=0)
    school_sslc=models.CharField(max_length=80)
    school_address_sslc=models.CharField(max_length=200)
    school_location=models.CharField(max_length=50)
    school_type=models.CharField(max_length=50)
    mediumstudy=models.CharField(max_length=50)
    sslcafter=models.CharField(max_length=50)
    sslc_year=models.IntegerField(default=0)
    sslc_marks=models.IntegerField(default=0)
    school_hsc=models.CharField(max_length=50)
    school_address_hsc=models.CharField(max_length=200)
    hsc_year=models.IntegerField(default=0)
    hsc_marks=models.IntegerField(default=0)
    hscschoollocation=models.CharField(max_length=50)
    hscschooltype=models.CharField(max_length=50)
    hscmediumstudy=models.CharField(max_length=50)
    maths_mark=models.IntegerField(default=0)
    physics_mark=models.IntegerField(default=0)
    chemistry_mark=models.IntegerField(default=0)
    cutoff=models.CharField(default=0,max_length=10)
    diploma_cgpa=models.IntegerField(default=0)
    college_diploma=models.CharField(max_length=80)
    TNEA_overall=models.IntegerField(default=0)
    TNEA_community=models.IntegerField(default=0)
    firstgraduate=models.CharField(max_length=50)
    physically_challenged=models.CharField(max_length=50)
    Disability=models.CharField(max_length=50)
    scholarship=models.CharField(max_length=50)
    scholarship_amount=models.IntegerField(default=0)
    eloan=models.CharField(max_length=50)
    education_loan=models.IntegerField(default=0)
    hostel=models.CharField(max_length=50)
    hostel_room=models.CharField(default=0,max_length=15)
    achievements=models.CharField(max_length=200)
    scholarship_details=models.CharField(max_length=200)
    extra_curricular=models.CharField(max_length=500)
    gender_user=models.CharField(max_length=50)
    dept=models.CharField(max_length=25,default='Mechatronics')
class certificate_details(models.Model):
    _userid=models.IntegerField(default=0)
    name=models.CharField(max_length=50)
    regno=models.CharField(max_length=50)
    startdate=models.CharField(max_length=50)
    enddate=models.CharField(max_length=50)
    eventtype=models.CharField(max_length=50)
    eventname=models.CharField(max_length=50)
    eventdays=models.IntegerField(default=0)
    location=models.CharField(max_length=100)