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
    LANDLORD = 'LANDLORD'
    AGENT = 'AGENT'
    ADMIN = 'ADMIN'
    TEST = 'TEST'
    
    USER_TYPE_CHOICES = (
        (TENANT, 'TENANT'),
        (LANDLORD, 'LANDLORD'),
        (AGENT, 'AGENT'),
        (ADMIN, 'ADMIN'),
        (TEST,'TEST')
    )
    
    user_type = models.CharField(max_length=64,choices=USER_TYPE_CHOICES,default=TEST)
    
    USER_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('VERIFIED', 'VERIFIED'),
        ('SUSPENDED', 'SUSPENDED'),
    )
    
    user_status  = models.CharField(max_length=64,choices=USER_STATUS_CHOICES,default='NEW')
    
    first_name  = models.CharField(max_length=256, blank=True)
    last_name  = models.CharField(max_length=256, blank=True)
    
    contact_number  = models.CharField(max_length=64, blank=True)
    email  = models.CharField(max_length=128, blank=True)
    
    user_id = models.CharField(max_length=256, default="FFFF")
    password = models.CharField(max_length=256, default="FFFF")
    secret_key = models.CharField(max_length=64, blank=True)
    password_reset_token  = models.CharField(max_length=512, blank=True)
    user_bsb  = models.CharField(max_length=64, blank=True)
    user_account_number  = models.CharField(max_length=128, blank=True)
    user_bank_name  = models.CharField(max_length=256, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    #verified_at  = models.DateTimeField(blank=True)
    
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.user_id, self.user_type, self.user_status, self.first_name, self.last_name, self.contact_number, self.email) 

    
"""
Application Model, model used for security deposits 
"""

class Application(models.Model): 

    APPLICATION_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('VERIFIED', 'VERIFIED'),
        ('ACTIVE', 'ACTIVE'),
        ('SUSPENDED', 'SUSPENDED'),
        ('DISPUTE', 'DISPUTE'),
        ('COMPLETE', 'COMPLETE'),
    )
    
    application_status  = models.CharField(max_length=64,choices=APPLICATION_STATUS_CHOICES,default='NEW')
    
    ejari_no = models.CharField(max_length=128)
    premise_no = models.CharField(max_length=128)
    internal_id = models.CharField(max_length=128)
    tenant_id  = models.CharField(max_length=512)
    owner_id  = models.CharField(max_length=512)
    
    application_address  = models.CharField(max_length=256)
    
    application_start_date  = models.DateTimeField(blank=True)
    application_end_date  = models.DateTimeField(blank=True)
    
    application_deposit_amount  = models.CharField(max_length=128,  blank=True)
    application_deposit_payment_terms  = models.CharField(max_length=64,  blank=True)
    application_deposit_holding  = models.CharField(max_length=64, blank=True)
    application_created_date  = models.DateTimeField(auto_now_add=True)
    
    application_tenant_dispute_claim = models.CharField(max_length=2048, blank=True)
    application_owner_dispute_claim = models.CharField(max_length=2048, blank=True)
    
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.application_id, self.internal_id, self.application_registered_by, self.application_other_party, self.application_deposit_amount, self.application_deposit_payment_terms, self.application_created_date)
    
    
"""
Event Model, model used for recording Events
"""

class Event(models.Model):
    
    EVENT_STATUS_CHOICES = (
        ('NEW', 'NEW'),
        ('HANDLED', 'HANDLED'),
        ('IGNORED', 'IGNORED'),
    )
    
    event_status  = models.CharField(max_length=512,choices=EVENT_STATUS_CHOICES,default='NEW')
    
    event_id = models.CharField(max_length=128)
    event_type = models.CharField(max_length=64)
    user_id  = models.CharField(max_length=512)
    event_occured_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.event_id, self.event_type, self.user_id, self.event_status, self.event_occured_at)
    
    
 
    
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
    
    
    


    

    
    
    
    
