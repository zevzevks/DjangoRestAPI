from rest_framework import serializers
from .models import AdultTrain

class AdultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdultTrain
        fields = ['record_id','age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week',
                  'country','proxy','target','part_date']