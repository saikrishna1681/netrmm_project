from django.db import models

# Create your models here.

class Script(models.Model):

    name=models.CharField(max_length=100,null=False,blank=False)
    body=models.TextField()

    def __str__(self):

        return f'{self.id}____{self.name}'

class ExecutionLog(models.Model):

    script=models.ForeignKey(Script,on_delete=models.CASCADE, related_name="script")
    output=models.CharField(max_length=1)
    starttime=models.DateTimeField()
    endtime=models.DateTimeField()
    duration=models.DecimalField(max_digits=17, decimal_places=7)

    def __str__(self):

        return f'{self.id}'