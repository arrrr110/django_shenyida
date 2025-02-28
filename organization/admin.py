# admin.py
from django.contrib import admin
from .models import OrgCustomTestSchemeMapping

@admin.register(OrgCustomTestSchemeMapping)
class OrgCustomTestSchemeMappingAdmin(admin.ModelAdmin):
    """
    机构自定义组合检测项目方案的管理界面配置
    """
    # 在列表页显示的字段
    list_display = ('coop_org_user_records_id', 'package_name', 'detection_projects')
    # 可用于搜索的字段
    search_fields = ('package_name', 'detection_projects', 'description')
    # 过滤字段
    list_filter = ('coop_org_user_records_id',)
    # 编辑页的字段分组
    fieldsets = (
        (None, {
            'fields': ('coop_org_user_records_id', 'package_name')
        }),
        ('检测项目信息', {
            'fields': ('detection_projects', 'description')
        }),
    )