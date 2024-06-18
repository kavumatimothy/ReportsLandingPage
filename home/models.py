from django.db import models

# Create your models here.

department_choices = (
    ('Finance', 'Finance'),
    ('Monitoring and evaluation', 'Monitoring And Evaluation'),
    ('HR', 'Human Resource'),
    ('Community', 'Community'),
    ('Clinical', 'Clinical'),
    ('Operations', 'Operations'),
    ('Research', 'Research'),
    ('Communications', 'Communications'),
    ('Informatics and IT', 'Informatics and IT'),
    ('Cross_Cutting', 'Cross_Cutting')

)


class Department(models.Model):
    department_name = models.CharField(max_length=200, choices=department_choices, unique=True)
    date_created    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.department_name


class Report(models.Model):
    report_name  = models.CharField(max_length=200,unique=True)
    link_address = models.CharField(max_length=200,unique=True)
    report_detail= models.CharField(max_length=200, blank=True)
    department   = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.report_name
