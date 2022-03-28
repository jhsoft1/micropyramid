from django.db import models


# https://micropyramid.com/blog/understanding-djangos-model-formsets-in-detail-and-their-advanced-usage/
class Group(models.Model):
    business_profile_id = models.CharField(max_length=50)

    def __str__(self):
        return self.business_profile_id


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.user_group} {self.birth_date}'
