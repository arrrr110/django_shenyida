# admin.py

from django.contrib import admin
from .models import Device, HealthData, TestTransactionInfo, UserCheckupSingleRecords

# 自定义截断显示函数
def truncate_value(value):
    if value and len(str(value)) > 5:
        return str(value)[:5] + '...'
    return value

# 注册 Device 模型到 Django 管理后台
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """
    设备模型的管理类，用于在 Django 管理后台展示设备信息
    """
    # 显示所有字段
    list_display = [
        'device_model', 'unit_name', 'unit_no', 'mac_addr', 'device_no'
    ]
    # 搜索字段
    search_fields = ['device_model', 'unit_name', 'unit_no', 'mac_addr', 'device_no']

# 注册 HealthData 模型到 Django 管理后台
@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    """
    健康数据模型的管理类，用于在 Django 管理后台展示健康数据信息
    """
    # 自定义显示方法 省略展示内容
    def address_display(self, obj):
        return truncate_value(obj.address)

    address_display.short_description = '地址'

    # 显示所有字段
    list_display = [
        'device', 'data_type', 'user_id',  'name', 'measure_time', 'record_no', 'bpm_n', 'bpm_s', 'bpm', 'xy_n', 'xy_s', 'xy',
        'hrR_s', 'sbpR_n', 'dbpR_s', 'dbpR', 'sbpR', 'hrR', 'sbpR_s', 'hrR_n',
        'dbpR_n', 'bmi_s', 'bmi', 'height', 'nation', 'weight', 'weight_n',
        'weight_s', 'start_date', 'end_date', 'department', 'bmi_n', 'address_display',
        'login_type', 'birthday', 'age', 'sex'
    ]
    # 搜索字段
    search_fields = [
        'device__device_no', 'data_type', 'user_id', 'name', 'record_no'
    ]
    # 过滤字段
    list_filter = ['data_type', 'measure_time']

# new 2025-2-28
# syd_store/admin.py

# 定义一个辅助函数，用于获取模型的所有字段名
def get_all_field_names(model):
    return [field.name for field in model._meta.fields]

@admin.register(TestTransactionInfo)
class TestTransactionInfoAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(TestTransactionInfo)
    search_fields = get_all_field_names(TestTransactionInfo)

@admin.register(UserCheckupSingleRecords)
class UserCheckupSingleRecordsAdmin(admin.ModelAdmin):
    list_display = get_all_field_names(UserCheckupSingleRecords)
    search_fields = get_all_field_names(UserCheckupSingleRecords)