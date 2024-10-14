from django.db import models


class Chitosan_Productions(models.Model):
    name     = models.CharField(max_length=100)
    purpose  = models.CharField(max_length=100)
    purity   = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    form     = models.CharField(max_length=100)

    ## REPORT STATUS (4 teams)
    deprotein_report       = models.BooleanField(default=False)
    deproteint_report_mng  = models.BooleanField(default=False)

    mineral_report         = models.BooleanField(default=False)
    mineral_report_c1      = models.BooleanField(default=False)
    mineral_report_mng     = models.BooleanField(default=False)


    deacetyl_report        = models.BooleanField(default=False)
    deacetyl_report_c1        = models.BooleanField(default=False)
    deacetyl_report_mng    = models.BooleanField(default=False)

    chitosan_method        = models.BooleanField(default=False)
    chitosan_report        = models.BooleanField(default=False)
    chitosan_encrypt       = models.BooleanField(default=False)
    key_sent  = models.BooleanField(default=False)
    chitosan_report_mng    = models.BooleanField(default=False)


    ### MODULE 1 -Report
    Shell_Type          = models.CharField(max_length=100,null=True)
    Processing_Method   = models.CharField(max_length=100,null=True)
    NaOH_Concentration  = models.CharField(max_length=100,null=True)
    Treatment_Time      = models.CharField(max_length=100,null=True)
    Moisture_Loss       = models.CharField(max_length=100,null=True)
    NaOH_Quantity       = models.CharField(max_length=100,null=True)


    ### MODULE 2 -- REPORT
    Mineraltype = models.CharField(max_length=100, null=True)
    Separation_Method = models.CharField(max_length=100, null=True)
    Reagent_Used = models.CharField(max_length=100, null=True)
    Reagent_Concentration = models.CharField(max_length=100, null=True)
    Separation_Time = models.CharField(max_length=100, null=True)
    Energy_Consumption = models.CharField(max_length=100, null=True)
    min_efficiency = models.CharField(max_length=100, null=True)

    #### Module 3 Report
    Deacetylation_Method = models.CharField(max_length=100, null=True)
    Reaction_Temperature = models.CharField(max_length=100, null=True)
    Reaction_Time = models.CharField(max_length=100, null=True)
    Degree_Deacetylation = models.CharField(max_length=100, null=True)
    Ash_Content = models.CharField(max_length=100, null=True)
    deacetyl_efficiency = models.CharField(max_length=100, null=True)

    ### Module 4 Report
    chitosan_extract_method    = models.CharField(max_length=100, null=True)
    chit_reagent  = models.CharField(max_length=100, null=True)
    viscosity                   = models.CharField(max_length=100, null=True)
    chit_reagent_concentration  = models.CharField(max_length=100, null=True)
    chitosan_efficiency  = models.CharField(max_length=100, null=True)
    process_time  = models.CharField(max_length=100, null=True)
    encryption_key = models.CharField(max_length=100, null=True)

    ### Encrypted Value
    block_hash = models.CharField(max_length=64, blank=True, null=True)
    encrypted_chitosan_extract_method = models.TextField(blank=True, null=True)
    encrypted_chit_reagent = models.TextField(blank=True, null=True)
    encrypted_viscosity = models.TextField(blank=True, null=True)
    encrypted_chit_reagent_concentration = models.TextField(blank=True, null=True)
    encrypted_chitosan_efficiency = models.TextField(blank=True, null=True)

    ## REPORT
    report_path = models.CharField(max_length=500, null=True)
    Image_graph = models.CharField(max_length=500, null=True)
