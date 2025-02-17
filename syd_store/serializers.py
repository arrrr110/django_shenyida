from rest_framework import serializers
from .models import Device, HealthData

# 设备序列化器
class DeviceSerializer(serializers.ModelSerializer):
    """
    设备模型的序列化器，用于将Device模型实例转换为JSON数据
    """
    class Meta:
        model = Device
        fields = '__all__'  # 序列化所有字段

# 健康数据序列化器
class HealthDataSerializer(serializers.ModelSerializer):
    """
    健康数据模型的序列化器，用于将HealthData模型实例转换为JSON数据
    """
    device = DeviceSerializer()  # 嵌套序列化Device对象

    class Meta:
        model = HealthData
        fields = '__all__'  # 序列化所有字段