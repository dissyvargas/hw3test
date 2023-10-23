from django.db import models

# Create your models here.
class Degree(models.Model): 
    major_code = models.IntegerField(help_text="Major ID #")
    degree_name = models.CharField(max_length=200, help_text="Degree name")
    college_name = models.CharField(max_length=200, help_text="College name")

    def __str__(self):
        return self.major_code
 
class requiredCourses(models.Model):
    subject_name = models.CharField(max_length=200, help_text="Subject name")
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    hours = models.IntegerField(help_text="hours required in subject")
    classes_offered = models.CharField(max_length=200, help_text="classes offered")

    def __str__(self):
        return self.subject_name
    
class degreeSpecific(models.Model):
    name = models.CharField(max_length=200, help_text="Subject name")
    classCode = models.IntegerField(help_text="class ID #")
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    hours = models.IntegerField(help_text="hours required in subject")
  

    def __str__(self):
        return self.name
    

