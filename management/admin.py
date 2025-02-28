# admin.py

from django.contrib import admin
from .models import TestTypeMapping, DeviceRecords, ArticleRecords


# 注册 TestTypeMapping 模型到 Django 管理界面
@admin.register(TestTypeMapping)
class TestTypeMappingAdmin(admin.ModelAdmin):
    """
    检测项目类型表的管理类
    """
    # 在列表视图中显示的字段
    list_display = ('detection_name', 'normal_range', 'unit_of_measurement', 'feature_field')
    # 可用于搜索的字段
    search_fields = ('detection_name', 'feature_field')
    # 过滤字段
    list_filter = ('detection_name',)


# 注册 DeviceRecords 模型到 Django 管理界面
@admin.register(DeviceRecords)
class DeviceRecordsAdmin(admin.ModelAdmin):
    """
    设备库存表的管理类
    """
    # 在列表视图中显示的字段
    list_display = ('coop_org_user_records_id', 'device_deployment_address', 'device_type', 'device_number')
    # 可用于搜索的字段
    search_fields = ('device_number', 'device_type')
    # 过滤字段
    list_filter = ('device_type',)


# 注册 ArticleRecords 模型到 Django 管理界面
@admin.register(ArticleRecords)
class ArticleRecordsAdmin(admin.ModelAdmin):
    """
    科普文章表的管理类
    """
    # 在列表视图中显示的字段
    list_display = ('article_title', 'detection_project_type_id')
    # 可用于搜索的字段
    search_fields = ('article_title',)
    # 过滤字段
    list_filter = ('detection_project_type_id',)
