from django.contrib import admin
from .models import Device, BloodOxygen, BloodPressure, HeightWeight

# 设备模型的 ModelAdmin 类
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_model', 'unit_name', 'unit_no', 'mac_addr', 'device_no')

# 血氧模型的 ModelAdmin 类
class BloodOxygenAdmin(admin.ModelAdmin):
    list_display = ('device', 'xy_n', 'address', 'user_id', 'login_type', 'measure_time', 'birthday', 'bpm', 'xy_s', 'xy', 'age', 'bpm_n', 'name', 'bpm_s', 'sex', 'record_no')

# 血压模型的 ModelAdmin 类
class BloodPressureAdmin(admin.ModelAdmin):
    list_display = ('device', 'address', 'user_id', 'login_type', 'hrR_s', 'sbpR_n', 'measure_time', 'dbpR_s', 'dbpR', 'sbpR', 'hrR', 'birthday', 'age', 'sbpR_s', 'name', 'sex', 'hrR_n', 'record_no', 'dbpR_n')

# 身高体重模型的 ModelAdmin 类
class HeightWeightAdmin(admin.ModelAdmin):
    list_display = ('device', 'address', 'user_id', 'login_type', 'measure_time', 'bmi_s', 'bmi', 'height', 'nation', 'birthday', 'weight', 'age', 'weight_n', 'name', 'weight_s', 'start_date', 'end_date', 'sex', 'department', 'record_no', 'bmi_n')

# 注册模型和对应的 ModelAdmin 类
admin.site.register(Device, DeviceAdmin)
admin.site.register(BloodOxygen, BloodOxygenAdmin)
admin.site.register(BloodPressure, BloodPressureAdmin)
admin.site.register(HeightWeight, HeightWeightAdmin)