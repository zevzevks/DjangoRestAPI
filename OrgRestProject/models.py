from email.policy import default
from django.db import models

 
class AdultTrain(models.Model):
    record_id = models.Field(db_column='RECORD_ID',primary_key = True)
    age = models.IntegerField(db_column='AGE', blank=True, null=True, default='')  # Field name made lowercase.
    workclass = models.TextField(db_column='WORKCLASS', blank=True, null=True, default='')  # Field name made lowercase.
    fnlwgt = models.IntegerField(db_column='FNLWGT', blank=True, null=True, default='')  # Field name made lowercase.
    education = models.TextField(db_column='EDUCATION', blank=True, null=True, default='')  # Field name made lowercase.
    education_num = models.IntegerField(db_column='EDUCATION_NUM', blank=True, null=True, default='')  # Field name made lowercase.
    marital_status = models.TextField(db_column='MARITAL_STATUS', blank=True, null=True, default='')  # Field name made lowercase.
    occupation = models.TextField(db_column='OCCUPATION', blank=True, null=True, default='')  # Field name made lowercase.
    relationship = models.TextField(db_column='RELATIONSHIP', blank=True, null=True, default='')  # Field name made lowercase.
    race = models.TextField(db_column='RACE', blank=True, null=True, default='')  # Field name made lowercase.
    sex = models.TextField(db_column='SEX', blank=True, null=True, default='')  # Field name made lowercase.
    capital_gain = models.IntegerField(db_column='CAPITAL_GAIN', blank=True, null=True, default='')  # Field name made lowercase.
    capital_loss = models.IntegerField(db_column='CAPITAL_LOSS', blank=True, null=True, default='')  # Field name made lowercase.
    hours_per_week = models.IntegerField(db_column='HOURS_PER_WEEK', blank=True, null=True, default='')  # Field name made lowercase.
    country = models.TextField(db_column='COUNTRY', blank=True, null=True, default='')  # Field name made lowercase.
    proxy = models.TextField(db_column='PROXY', blank=True, null=True, default='')  # Field name made lowercase.
    target = models.IntegerField(db_column='TARGET', blank=True, null=True, default='')  # Field name made lowercase.
    part_date = models.TextField(db_column='PART_DATE', blank=True, null=True, default='')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADULT_TRAIN'