from django.db import models
from django.contrib.auth.models import User


class OrgCustomTestSchemeMapping(models.Model):
    """
    机构自定义组合检测项目方案
    """
    # 默认配置'自增主键'
    coop_org_user_records_id = models.ForeignKey(User, models.SET_NULL,  blank=True, null=True, verbose_name='所属机构外键')
    package_name = models.CharField(blank=True, null=True, max_length=100, verbose_name='自定义套餐名称')
    detection_projects = models.TextField(blank=True, null=True, verbose_name='包含的检测项目类型')
    # 多个项目以'_'连接,用于后续约束
    # 废弃 is_default = models.BooleanField(default=False, verbose_name='是否为默认全选方案')
    description = models.TextField(blank=True, null=True, verbose_name='套餐详细描述')

    class Meta:
        verbose_name = '机构自定义检测项目方案'
        verbose_name_plural = '机构自定义检测项目方案'