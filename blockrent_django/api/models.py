from django.db import models
import uuid 

# Create your models here.

"""
User Model, there are three types of users:
    1. Tenant
    2. Landlord
    3. Property Agent
"""

class User(models.Model):
    
    TENANT = 'TENANT'
    LANDLORD = 'LLANDLORD'
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
    
    first_name  = models.CharField(max_length=256)
    last_name  = models.CharField(max_length=256)
    
    ##excuse my shit way of doing this, randomly generating user_id
    random_uid = str(uuid.uuid4())
    generated_user_id = str(first_name)[0] + str(last_name)[0] + random_uid[0] + random_uid[1] + random_uid[2] + random_uid[3]
    generated_password =  random_uid[4] + random_uid[5] + random_uid[6] + random_uid[7] + str(first_name)[0] + str(last_name)[0] 
    
    contact_number  = models.CharField(max_length=64)
    email  = models.CharField(max_length=128)


    user_id = models.CharField(max_length=256, default=generated_user_id)
    password = models.CharField(max_length=256, default=generated_password)
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
    
    ##excuse my shit way of doing this, randomly generating random id
    random_uid = str(uuid.uuid4())
    generated_internal_id = random_uid[0] + random_uid[1] + random_uid[2] + random_uid[3]
    internal_id = models.CharField(max_length=64, default=generated_internal_id)
    
    application_id = models.CharField(max_length=128)
    tenant_id  = models.CharField(max_length=512)
    onwer_id  = models.CharField(max_length=512)
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
        return '%s %s %s %s %s %s %s' % (self.application_id, self.internal_id, self.tenant_id, self.onwer_id, self.application_deposit_amount, self.application_deposit_payment_terms, self.application_created_date)
    
    
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
    
    
    
    
