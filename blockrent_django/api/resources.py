# api/resources.py

from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.validation import Validation
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from api.models import User
from api.models import Application
from api.models import Event
from api.models import Registration
import uuid 




    
    
"""
user fields:
    user_id
    secret_key
    password
    password_reset_token
    first_name
    last_name
    contact_number
    email
    user_type
    user_status
    user_bsb
    user_account_number
    user_bank_name
    created_at
    verified_at
"""

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'user_id': 'exact',
            'first_name': 'iexact',
            'last_name': 'iexact',
            'email': 'iexact',
            'user_type': ALL,
            'user_status': ALL,
        }
        
        
   
    
    
"""
Application fields:
    application_id
    internal_id
    tenant_id
    onwer_id
    application_address
    application_start_date
    application_end_date
    application_deposit_amount
    application_deposit_payment_terms
    application_status
    application_deposit_holding
    application_created_date
"""
        
class ApplicationResource(ModelResource):
    class Meta:
        queryset = Application.objects.all()
        resource_name = 'application'
        authorization = Authorization()
        filtering = {
            'application_id': 'exact',
            'internal_id': 'iexact',
            'tenant_id': 'exact',
            'onwer_id': 'iexact',
            'application_status': ALL,
            'application_address': ALL,
        }

  
"""
Event fields:
    event_id
    event_type
    user_id
    event_status
    event_occured_at
"""


      
class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        authorization = Authorization()
        filtering = {
            'event_id': 'exact',
            'event_type': 'iexact',
            'user_id': 'iexact',
            'email': 'iexact',
            'event_status': ALL,
        }
        
        
        
"""
Registration Handler

"""


class RegistrationResource(ModelResource):
    
    class Meta:
        queryset = Registration.objects.all()
        resource_name = 'registration'
        authorization = Authorization()
        allowed_methods = ['post']
        
    def obj_create(self, bundle, request=None, **kwargs):
    
        
        tenant_first_name = bundle.data['tenantDetails']['firstName']
        tenant_last_name = bundle.data['tenantDetails']['lastName']
        owner_first_name = bundle.data['ownerDetails']['firstName']
        owner_last_name = bundle.data['ownerDetails']['lastName']
        

        try: ##try to find if registrant user exist
             tenant = User.objects.get(
                     first_name=tenant_first_name,
                     last_name=tenant_last_name,
                     email=bundle.data['tenantDetails']['email'])
             
             generated_tenant_id = tenant.user_id 
        except User.DoesNotExist: ##if doesn't exist create a new object
            
            ##excuse my shit way of doing this, randomly generating user_id
            random_uid = str(uuid.uuid4())
            generated_tenant_id = str(tenant_first_name)[0] + str(tenant_last_name)[0] + random_uid[0] + random_uid[1] + random_uid[2] + random_uid[3]
            generated_tenant_password =  random_uid[4] + random_uid[5] + random_uid[6] + random_uid[7] + str(tenant_first_name)[0] + str(tenant_last_name)[0] 
            
            tenant = User(
                     user_id=generated_tenant_id,
                     password=generated_tenant_password,
                     user_type="TENANT",
                     first_name=bundle.data['tenantDetails']['firstName'],
                     last_name=bundle.data['tenantDetails']['lastName'],
                     contact_number=bundle.data['tenantDetails']['phone'],
                     email=bundle.data['tenantDetails']['email'])
            tenant.save()
            
            
        try: ##try to find if owner user exist
             owner = User.objects.get(
                     first_name=owner_first_name,
                     last_name=owner_last_name, 
                     email=bundle.data['ownerDetails']['email'])
             
             generated_owner_id = owner.user_id 
        except User.DoesNotExist: ##if doesn't exist create a new object
            
            random_uid = str(uuid.uuid4())
            generated_owner_id = str(owner_first_name)[0] + str(owner_last_name)[0] + random_uid[0] + random_uid[1] + random_uid[2] + random_uid[3]
            generated_owner_password =  random_uid[4] + random_uid[5] + random_uid[6] + random_uid[7] + str(owner_first_name)[0] + str(owner_last_name)[0] 
            
            owner = User(
                     user_id=generated_owner_id,
                     password=generated_owner_password,
                     user_type="LANDLORD",
                     first_name=bundle.data['ownerDetails']['firstName'],
                     last_name=bundle.data['ownerDetails']['lastName'],
                     contact_number=bundle.data['ownerDetails']['phone'],
                     email=bundle.data['ownerDetails']['email'])
            owner.save()
            
            
        try: ##try to find if application allready exist
             owner = Application.objects.get(ejari_no=bundle.data['leaseApplicationDetails']['ejariNo'])     
        except Application.DoesNotExist: ##if doesn't exist create a new object
            new_application = Application(
                     ejari_no=bundle.data['leaseApplicationDetails']['ejariNo'],
                     premise_no=bundle.data['leaseApplicationDetails']['premiseNo'],
                     internal_id=bundle.data['leaseApplicationDetails']['id'],
                     tenant_id=generated_tenant_id,
                     owner_id=generated_owner_id,
                     application_deposit_amount=bundle.data['leaseApplicationDetails']['depositAmount'],
                     application_address=bundle.data['leaseApplicationDetails']['id'],
                     application_start_date=bundle.data['leaseApplicationDetails']['startDate'],
                     application_end_date=bundle.data['leaseApplicationDetails']['endDate']
                     )
            new_application.save()
        
       
    
        
        


     
        
