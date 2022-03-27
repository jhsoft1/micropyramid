from django.db import models


# https://micropyramid.com/blog/understanding-djangos-model-formsets-in-detail-and-their-advanced-usage/
class Group(models.Model):
    name = models.CharField()


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
