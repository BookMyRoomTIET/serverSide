from posixpath import basename
from django.db import models

Gender = [
        ('Male','Male'),
        ('Female','Female')
    ]


class hostelInformationModel(models.Model):
    hostelName = models.CharField(max_length=100)
    hostel_id = models.CharField(primary_key=True, max_length=10)
    hostel_type = models.CharField(max_length=10,choices=Gender,blank=True,null=True)
    warden_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(max_length=10)
    contact_email = models.EmailField(max_length=100)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.hostelName

class hostelImagesModel(models.Model):
    hostel = models.ForeignKey(hostelInformationModel, on_delete=models.CASCADE, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.hostel)

class hostelMapModel(models.Model):
    hostel_id = models.ForeignKey(hostelInformationModel, on_delete=models.CASCADE)
    mapLink = models.CharField(max_length=1000,unique=True)

    def __str__(self):
        return self.hostel_id.hostelName

class hostelAllocatedToYear(models.Model):
    gradYear = models.IntegerField()
    gender = models.CharField(max_length=100, choices=Gender)
    hostel_id = models.ForeignKey(hostelInformationModel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gradYear)+" "+self.gender

class hostelPreferenceFirstYear(models.Model):
    name = models.CharField(max_length=100)
    rollNumber = models.IntegerField()
    cgpa = models.FloatField()
    preferenceOne = models.CharField(max_length=100)
    preferenceTwo = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class hostelPreferenceSecondYear(models.Model):
    name = models.CharField(max_length=100)
    rollNumber = models.IntegerField()
    cgpa = models.FloatField()
    preferenceOne = models.CharField(max_length=100)
    preferenceTwo = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomInformationModel(models.Model):
    hostel_id = models.ForeignKey(hostelInformationModel, on_delete=models.CASCADE)
    room_id = models.CharField(max_length=10,unique=True)
    room_type = models.CharField(max_length=100)
    room_capacity = models.IntegerField(max_length=10)
    room_price = models.IntegerField(max_length=10)
    room_status = models.CharField(max_length=100)
