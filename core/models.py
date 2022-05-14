from django.db import models
from enum import Enum
# Create your models here.


class BloodType(Enum):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    OTHER = 'Other'

    # ('A+', 'A+',),
    # ('A-', 'A-'),
    # ('B+', 'B+'),
    # ('B-', 'B-'),
    # ('O+', 'O+'),
    # ('O-', 'O-'),
    # ('AB+', 'AB+'),
    # ('AB-', 'AB-'),
    # ('Other', 'Other'),


_bloodTypes = []
for t in BloodType:
    _bloodTypes.append((t.name, t.name))


class Person(models.Model):

    fullName = models.CharField(max_length=255)
    birthdate = models.DateField()
    address = models.CharField(max_length=255)
    bloodType = models.CharField(
        max_length=20, choices=_bloodTypes, default=BloodType.O_POSITIVE.name)
    # bloodType = models.CharField(max_length=10, choices=_bloodTypes)

    class Meta:
        abstract = True


class BloodDonor(Person):
    pass


class BloodReceiver(Person):
    pass


class Examiner(Person):
    pass


class BloodSample(models.Model):
    pass


class BloodWork(models.Model):
    pass


class MedicalRecord(models.Model):
    pass
