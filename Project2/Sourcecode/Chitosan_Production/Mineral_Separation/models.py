from django.db import models

# Create your models here.


class Mineral_teams(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    mineral_login_approve = models.BooleanField(null=True,default=False)
    mineral_team_id = models.CharField(max_length=100, unique=True, null=True)


class Mineral_dataset(models.Model):
    name        = models.CharField(max_length=100)
    purpose     = models.CharField(max_length=100)
    purity      = models.CharField(max_length=100)
    quantity    = models.CharField(max_length=100)
    form        = models.CharField(max_length=100)

    #####
    Mineraltype       = models.CharField(max_length=100)
    Separation_Method = models.CharField(max_length=100)
    Reagent_Used      = models.CharField(max_length=100)
    Reagent_Concentration = models.CharField(max_length=100)
    Separation_Time     = models.CharField(max_length=100)
    Energy_Consumption = models.CharField(max_length=100)
