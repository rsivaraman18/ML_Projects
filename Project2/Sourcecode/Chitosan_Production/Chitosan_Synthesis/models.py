from django.db import models

# Create your models here.
class Chitosan_teams(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    chitosan_login_approve = models.BooleanField(null=True,default=False)
    chitosan_team_id = models.CharField(max_length=100, unique=True, null=True)
