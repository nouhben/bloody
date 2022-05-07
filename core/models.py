from django.db import models

# Create your models here.


class BloodType:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name.upper()


class Person(models.Model):
    _bloodTypes = [
        ('A+', 'A+',),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('Other', 'Other'),
    ]
    fullName = models.CharField(max_length=255)
    birthdate = models.DateField()
    address = models.CharField(max_length=255)
    bloodType = models.CharField(max_length=10, choices=_bloodTypes)

    class Meta:
        abstract = True


class BloodDonor(Person):
    pass


class BloodReceiver(Person):
    pass
