from django.db import models

# Create your models here.
class Deacetyl_teams(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    deacetyl_login_approve = models.BooleanField(null=True,default=False)
    deacetyl_team_id = models.CharField(max_length=100, unique=True, null=True)


#
class Deacetylation_dataset(models.Model):
    purpose = models.CharField(max_length=100)
    purity = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    form = models.CharField(max_length=100)

    Deacetylation_Method = models.CharField(max_length=100)
    Reaction_Temperature = models.CharField(max_length=100)
    Reaction_Time        = models.CharField(max_length=100)
    Degree_Deacetylation = models.CharField(max_length=100)
    Ash_Content          = models.CharField(max_length=100)


