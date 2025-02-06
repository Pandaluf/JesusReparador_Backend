from rest_framework import serializers

from complaint.models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Complaint