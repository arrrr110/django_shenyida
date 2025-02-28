# admin.py
from django.contrib import admin
from .models import LogAuditInfo

# 自定义 LogAuditInfo 的管理类
@admin.register(LogAuditInfo)
class LogAuditInfoAdmin(admin.ModelAdmin):
    # 在列表页面显示的字段
    list_display = ('table_name', 'data_id', 'operator_id', 'operation_time')
    # 可以根据这些字段进行搜索
    search_fields = ('table_name', 'data_id', 'operator_id')
    # 按这些字段进行过滤
    list_filter = ('table_name', 'operation_time')
    # 日期分层导航，按操作时间进行分层
    date_hierarchy = 'operation_time'
    # 只读字段，不允许在管理界面中编辑
    readonly_fields = ('operation_time',)

    # 自定义显示操作前和操作后数据的字段
    def before_data_display(self, obj):
        """显示操作前的数据，截断显示避免过长"""
        return str(obj.before_data)[:50] + '...' if len(str(obj.before_data)) > 50 else str(obj.before_data)
    before_data_display.short_description = '操作前数据（截断）'

    def after_data_display(self, obj):
        """显示操作后的数据，截断显示避免过长"""
        return str(obj.after_data)[:50] + '...' if len(str(obj.after_data)) > 50 else str(obj.after_data)
    after_data_display.short_description = '操作后数据（截断）'

    # 额外显示的字段
    fieldsets = (
        (None, {
            'fields': ('table_name', 'data_id', 'operator_id')
        }),
        ('数据变更', {
            'fields': ('before_data_display', 'after_data_display')
        }),
        ('时间信息', {
            'fields': ('operation_time',)
        }),
    )