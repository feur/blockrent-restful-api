# api/resources.py

from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from api.models import User
from api.models import Application
from api.models import Event



    
    
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
        filtering = {
            'user_id': 'exact',
            'first_name': 'iexact',
            'last_name': 'iexact',
            'email': 'iexact',
            'user_type': ALL,
            'user_status': ALL,
        }
        
        
   
    
    
"""
Applicaiton fields:
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
        
     
        
