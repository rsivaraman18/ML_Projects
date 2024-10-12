from django.db import models

# Create your models here.


class Deprotein_teams(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    deprotein_login_approve = models.BooleanField(null=True,default=False)
    deprotein_team_id = models.CharField(max_length=100, unique=True, null=True)






class Deprotein_dataset(models.Model):
    purpose   = models.CharField(max_length=100)
    purity    = models.CharField(max_length=100)
    quantity  = models.CharField(max_length=100)
    form      = models.CharField(max_length=100)

    Shell_Type           = models.CharField(max_length=100)
    Processing_Method    = models.CharField(max_length=100)
    NaOH_Concentration   = models.CharField(max_length=100)
    Treatment_Time       = models.CharField(max_length=100)
    Moisture_Loss        = models.CharField(max_length=100)
    NaOH_Quantity        = models.CharField(max_length=100)