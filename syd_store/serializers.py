# serializers.py
from rest_framework import serializers
from .models import Device, BloodOxygen, BloodPressure, HeightWeight

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class BloodOxygenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodOxygen
        fields = '__all__'

class BloodPressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodPressure
        fields = '__all__'

class HeightWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeightWeight
        fields = '__all__'