from django.db import models

# Create your models here.

department_choices = (
    ('finance', 'Finance'),
    ('monitoring and evaluation', 'Monitoring And Evaluation'),
    ('her', 'HR'),
    ('clinical', 'Clinical'),
    ('research', 'Research'),
    ('Informatics', 'Informatics')
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
