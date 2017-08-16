from rest_framework import serializers

from blood_alert.models import Alert


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ('name', 'blood_type', 'phone', 'location', 'date_time_posted','message','resolved')


