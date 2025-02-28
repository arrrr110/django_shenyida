from django.db import models
from django.contrib.auth.models import User


class TestTypeMapping(models.Model):
    """
    检测项目类型表
    """
    # 主键自动配置，不需要额外声明
    # id = models.AutoField(primary_key=True, verbose_name='主键')
    detection_name = models.CharField(max_length=50, verbose_name='检测项目具体名称')
    normal_range = models.CharField(max_length=50, blank=True, null=True, verbose_name='检测结果正常范围')
    unit_of_measurement = models.CharField(max_length=50, blank=True, null=True, verbose_name='检测结果计量单位')
    feature_field = models.CharField(max_length=50, verbose_name='检测项目相关特征字段')
    creator_instructions = models.TextField(blank=True, null=True, verbose_name='创建者说明信息')

    class Meta:
        ###
        # 默认情况下，Django 会根据应用名和模型名自动生成数据库表名，
        # 格式为 app_label_modelname（例如，应用名为 myapp，模型名为 ArticleRecords，
        # 则默认表名是 myapp_articlerecords）。使用 db_table 属性可以覆盖这个默认行为，
        # 自定义表名，使其更符合你的业务需求或数据库命名规范。
        # ###
        verbose_name = '检测项目类型映射'
        verbose_name_plural = '检测项目类型映射'


class DeviceRecords(models.Model):
    """
    设备库存表
    """
    # id = models.AutoField(primary_key=True, verbose_name='自增主键')
    coop_org_user_records_id = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name='所属体检机构外键')
    device_deployment_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='设备部署地址')
    device_type = models.CharField(max_length=50, blank=True, null=True, verbose_name='设备类型')
    device_number = models.CharField(max_length=50, verbose_name='设备编号')
    device_remark = models.TextField(blank=True, null=True, verbose_name='设备备注信息')

    class Meta:
        verbose_name = '设备库存记录'
        verbose_name_plural = '设备库存记录'


class ArticleRecords(models.Model):
    """
    科普文章表
    """
    # id = models.AutoField(primary_key=True, verbose_name='自增主键')
    article_title = models.CharField(max_length=50,verbose_name='科普文章标题')
    article_content = models.TextField(verbose_name='科普文章内容')
    detection_project_type_id = models.ForeignKey(
        TestTypeMapping, 
        models.SET_NULL, 
        blank=True, 
        null=True, 
        verbose_name='关键词'
        )

    class Meta:
        verbose_name = '科普文章'
        verbose_name_plural = '科普文章'

