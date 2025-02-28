# admin.py
from django.contrib import admin
from .models import UserTransactionInfo, UserBaseInfoRecords, UserRelativeRelationshipsRecords

# 注册 UserTransactionInfo 模型
@admin.register(UserTransactionInfo)
class UserTransactionInfoAdmin(admin.ModelAdmin):
    """
    管理用户建档事务表（主表）的管理类
    """
    # 在列表页面显示的字段
    list_display = ('openid', 'send_phone', 'coop_org_user_records_id', 'device_id', 'regist_time')
    # 可用于搜索的字段
    search_fields = ('openid', 'send_phone')
    # 过滤器
    list_filter = ('regist_time',)

# 注册 UserBaseInfoRecords 模型
@admin.register(UserBaseInfoRecords)
class UserBaseInfoRecordsAdmin(admin.ModelAdmin):
    """
    管理用户基础信息表(子表)的管理类
    """
    list_display = ('user_type', 'user_phone', 'name', 'birthday', 'address', 'gender', 'height', 'weight', 'is_deleted')
    search_fields = ('user_phone', 'name')
    list_filter = ('user_type', 'is_deleted')

# 注册 UserRelativeRelationshipsRecords 模型
@admin.register(UserRelativeRelationshipsRecords)
class UserRelativeRelationshipsRecordsAdmin(admin.ModelAdmin):
    """
    管理用户亲友关系表的管理类
    """
    list_display = ('transaction_info_id', 'user_base_info_id', 'relative_id', 'nicky_name', 'create_time')
    search_fields = ('nicky_name',)
    list_filter = ('create_time',)