from django.db import models


# Create your models here.


class Object(models.Model):
    ObjectID = models.IntegerField(primary_key=True)
    ObjectName = models.CharField(max_length=50)
    ObjectParent = models.CharField(max_length=50)
    IsTop = models.IntegerField(null=True)
    Handle_1 = models.IntegerField()
    Handle_2 = models.IntegerField()
    Handle_3 = models.IntegerField()
    ObjectRevision = models.IntegerField()

    def __str__(self):
        return str(self.ObjectName) + str(self.ObjectParent)

    class Meta:
        unique_together = (('Handle_1', 'Handle_2', 'Handle_3'),)


class Param(models.Model):
    ParamID = models.IntegerField()
    ObjectID = models.ForeignKey(Object, on_delete=models.CASCADE)
    ParamName = models.CharField(max_length=50)
    ParamValue = models.IntegerField()
    ParamCode = models.IntegerField()

    def __str__(self):
        return str(self.ParamName) + str(self.ParamValue)

    class Meta:
        unique_together = (('ParamID', 'ObjectID'),)
