from django.db import models
from django.utils import timezone


####
# 重点记录设备登记到机构的操作数据
# ##
class LogAuditInfo(models.Model):
    """
    操作日志表模型
    """
    table_name = models.CharField(max_length=255, verbose_name="操作所涉及的表名")
    data_id = models.IntegerField(verbose_name="操作的数据的 ID")
    operator_id = models.IntegerField(verbose_name="操作人员的 ID")
    before_data = models.JSONField(verbose_name="操作前的数据")
    after_data = models.JSONField(verbose_name="操作后的数据")
    operation_time = models.DateTimeField(auto_now_add=True, verbose_name="操作发生的具体时间")

    class Meta:
        verbose_name = "操作日志"
        verbose_name_plural = "操作日志"

    def __str__(self):
        return f"{self.table_name} - {self.data_id} 于 {self.operation_time} 被操作"