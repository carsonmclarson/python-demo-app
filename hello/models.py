from django.db import models
from heroku_connect.db import models as hc_models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    
class User(hc_models.HerokuConnectModel):
    sf_object_name = 'User'
    
    username = hc_models.Text(sf_field_name='Username', max_length=80)
    email = hc_models.Email(sf_field_name='Email')
    department = hc_models.Text(sf_field_name='Department', max_length=80)
    title = hc_models.Text(sf_field_name='Title', max_length=80)
