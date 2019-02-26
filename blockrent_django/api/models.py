from django.db import models


# Create your models here.

"""
User Model, there are three types of users:
    1. Tenant
    2. Landlord
    3. Property Agent
"""

class User(models.Model):
    
    TENANT = 'TENANT'
    OWNER = 'OWNER'
    ADMIN = 'ADMIN'
    TEST = 'TEST'
    
    USER_TYPE_CHOICES = (
        (TENANT, 'TENANT'),
        (OWNER, 'OWNER'),
        (ADMIN, 'ADMIN'),
        (TEST,'TEST')
    )
    
    accounType = models.CharField(max_length=64,choices=USER_TYPE_CHOICES,default=TEST)
    
    USER_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('VERIFIED', 'VERIFIED'),
        ('SUSPENDED', 'SUSPENDED'),
    )
    
    accountStatus  = models.CharField(max_length=64,choices=USER_STATUS_CHOICES,default='NEW')
    
    firstName  = models.CharField(max_length=256, blank=True)
    lastName  = models.CharField(max_length=256, blank=True)
    
    contactNumber  = models.CharField(max_length=64, blank=True)
    contactEmail  = models.CharField(max_length=128, blank=True)
    
    accountID = models.CharField(max_length=256, default="FFFF")
    password = models.CharField(max_length=256, default="FFFF")
    secret_key = models.CharField(max_length=64, blank=True)
    password_reset_token  = models.CharField(max_length=512, blank=True)
    bankBSB  = models.CharField(max_length=64, blank=True)
    bankNo  = models.CharField(max_length=128, blank=True)
    bankName  = models.CharField(max_length=256, blank=True)
    createdAt  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.user_id, self.user_type, self.user_status, self.first_name, self.last_name, self.contact_number, self.email) 

    
"""
Application Model, model used for security deposits 
"""

class Application(models.Model): 

    APPLICATION_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('CONFIRMED', 'CONFIRMED'),
        ('ACTIVE', 'ACTIVE'),
        ('SUSPENDED', 'SUSPENDED'),
        ('DISPUTE', 'DISPUTE'),
        ('COMPLETE', 'COMPLETE'),
    )
    
    status  = models.CharField(max_length=64,choices=APPLICATION_STATUS_CHOICES,default='NEW')
    isConfirmedByTenant = models.CharField(max_length=64,default="NO")
    isConfirmedByOwner = models.CharField(max_length=64,default="NO")
    
    ejariNo = models.CharField(max_length=128)
    premisNo = models.CharField(max_length=128)
    internalID = models.CharField(max_length=128)
    tenantID  = models.CharField(max_length=512)
    ownerID  = models.CharField(max_length=512)
    
    address  = models.CharField(max_length=256)
    
    statDate  = models.DateTimeField(blank=True)
    endDate  = models.DateTimeField(blank=True)
    
    depositAmount  = models.CharField(max_length=128,  blank=True)
    depositHolding  = models.CharField(max_length=64, blank=True)
    createdAt  = models.DateTimeField(auto_now_add=True)
    
    tenantDisputeClaim = models.CharField(max_length=2048, blank=True)
    ownerDisputeClaim = models.CharField(max_length=2048, blank=True)
    
    def __str__(self):
        return 1
    
    
"""
Event Model, model used for recording Events
"""

class Event(models.Model):
    
    EVENT_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('HANDLED', 'HANDLED'),
        ('IGNORED', 'IGNORED'),
    )
    
    status  = models.CharField(max_length=512,choices=EVENT_STATUS_CHOICES,default='NEW')
    
    referenceid = models.CharField(max_length=128, blank=True)
    what = models.CharField(max_length=64)
    who  = models.CharField(max_length=512)
    when  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 1
    
 
    
"""
Registration Model, model used for handling registration
"""    
    

class Registration(models.Model):
    
    USER_TYPE_CHOICES = (
        ('TENANT', 'TENANT'),
        ('LANDLORD', 'LANDLORD'),
        ('AGENT', 'AGENT'),
        ('ADMIN', 'ADMIN'),
        ('TEST','TEST')
    )
    
    registrant_type = models.CharField(max_length=64,choices=USER_TYPE_CHOICES,default='TEST')  
    registrant_first_name = models.DateTimeField(blank=True)
    registrant_last_name = models.DateTimeField(blank=True)
    registrant_phone = models.DateTimeField(blank=True)
    registrant_email = models.DateTimeField(blank=True)
    
    
    


    

    
    
    
    
