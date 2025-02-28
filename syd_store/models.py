from django.db import models
from management.models import TestTypeMapping, DeviceRecords
from django.contrib.auth.models import User


class TestTransactionInfo(models.Model):
    """
    体检业务事务表
    """
    user_id = models.CharField(max_length=50, verbose_name='用户的唯一标识', help_text='建档模式下，用户ID应为手机号，有助于后续和用户小程序匹配；游客模式下，用户ID默认为时间+随机数（例20250224141944225）')
    test_type_id = models.ForeignKey(TestTypeMapping, models.PROTECT, verbose_name='检测项目的唯一标识')
    coop_org_user_records_id = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name='体检机构的唯一标识')
    device_records_id = models.ForeignKey(DeviceRecords, models.PROTECT, verbose_name='体检设备的唯一标识', help_text='设备没有则自动建立数据')
    physical_examination_time = models.DateTimeField(auto_now_add=True, verbose_name='体检的具体时间')

    class Meta:
        verbose_name = '体检事务表'
        verbose_name_plural = '体检业务事务表（主表）'

    def __str__(self):
        return f"体检业务事务记录 {self.id}"


class UserCheckupSingleRecords(models.Model):
    """
    体检业务表
    """
    text_key = models.CharField(max_length=50, verbose_name='关联检测类型', help_text='如xy、hr等')
    text_value = models.CharField(max_length=255, verbose_name='关联检测的值', help_text='如\'96\'，\'阴性\'等')
    unit_of_measurement = models.CharField(max_length=50, verbose_name='字段单位', help_text='从检测项目类型表中获取')
    test_info_id = models.ForeignKey(TestTransactionInfo, models.PROTECT, verbose_name='事务表外键')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '体检业务表'
        verbose_name_plural = '体检业务表（子表）'

    def __str__(self):
        return f"体检业务子记录 {self.id}"
    
# 设备模型
class Device(models.Model):
    device_model = models.CharField(max_length=10, verbose_name='设备型号')
    unit_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='单位名称')
    unit_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='单位编号')
    mac_addr = models.CharField(max_length=20, blank=True, null=True, verbose_name='设备MAC地址')
    device_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='设备编号')

    def __str__(self):
        return self.device_no

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'

# 合并后的健康数据模型
class HealthData(models.Model):
    """
    test
    """
    # 数据类型枚举选项
    DATA_TYPE_CHOICES = [
        ('身高体重', '身高体重'),
        ('人体成分', '人体成分'),
        ('血压心率', '血压心率'),
        ('动脉硬化(动脉脉搏波速率)', '动脉硬化(动脉脉搏波速率)'),
        ('血糖尿酸胆固醇', '血糖尿酸胆固醇'),
        ('血糖', '血糖'),
        ('尿酸', '尿酸'),
        ('血红蛋白', '血红蛋白'),
        ('尿液分析', '尿液分析'),
        ('血氧测量', '血氧测量'),
        ('体温测量', '体温测量'),
        ('中医体质辨识', '中医体质辨识'),
        ('血脂四项', '血脂四项'),
        ('腰臀比', '腰臀比'),
        ('心电分析', '心电分析'),
        ('心理测试', '心理测试'),
        ('骨密度检测', '骨密度检测'),
        ('肺功能检测', '肺功能检测'),
        ('糖化血红蛋白检测', '糖化血红蛋白检测'),
        ('酒精含量检测', '酒精含量检测'),
        ('快速心电检测', '快速心电检测'),
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True, verbose_name='所属设备')
    # 数据类型
    data_type = models.CharField(max_length=50, choices=DATA_TYPE_CHOICES, blank=True, null=True, verbose_name='数据类型')

    # 心率相关
    bpm_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='心率正常范围')
    bpm_s = models.IntegerField(blank=True, null=True, verbose_name='心率状态码')
    bpm = models.IntegerField(blank=True, null=True, verbose_name='心率')
    # 血氧相关字段
    xy_n = models.CharField(blank=True, null=True, max_length=20, verbose_name='血氧正常范围')
    xy_s = models.IntegerField(blank=True, null=True, verbose_name='血氧状态码')
    xy = models.IntegerField(blank=True, null=True, verbose_name='血氧值')
    # 血压相关字段
    hrR_s = models.IntegerField(blank=True, null=True, verbose_name='心率状态码（血压）')
    sbpR_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='收缩压正常范围')
    dbpR_s = models.IntegerField(blank=True, null=True, verbose_name='舒张压状态码')
    dbpR = models.IntegerField(blank=True, null=True, verbose_name='舒张压值')
    sbpR = models.IntegerField(blank=True, null=True, verbose_name='收缩压值')
    hrR = models.IntegerField(blank=True, null=True, verbose_name='心率值（血压）')
    sbpR_s = models.IntegerField(blank=True, null=True, verbose_name='收缩压状态码')
    hrR_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='心率正常范围（血压）')
    dbpR_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='舒张压正常范围')
    # 身高体重相关字段
    bmi_s = models.IntegerField(blank=True, null=True, verbose_name='BMI状态码')
    bmi = models.FloatField(blank=True, null=True, verbose_name='BMI值')
    height = models.FloatField(blank=True, null=True, verbose_name='身高')
    nation = models.CharField(max_length=20, blank=True, null=True, verbose_name='民族')
    weight = models.FloatField(blank=True, null=True, verbose_name='体重')
    weight_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='体重正常范围')
    weight_s = models.IntegerField(blank=True, null=True, verbose_name='体重状态码')
    start_date = models.DateField(blank=True, null=True, verbose_name='开始日期')
    end_date = models.DateField(blank=True, null=True, verbose_name='结束日期')
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name='部门')
    bmi_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='BMI正常范围')
    # 公共字段
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='地址')
    user_id = models.CharField(max_length=20, verbose_name='用户ID')
    login_type = models.CharField(max_length=1, blank=True, null=True, verbose_name='登录类型')
    measure_time = models.DateTimeField(blank=True, null=True, verbose_name='测量时间')
    birthday = models.CharField(max_length=10, blank=True, null=True, verbose_name='生日')
    age = models.IntegerField(blank=True, null=True, verbose_name='年龄')
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='姓名')
    sex = models.CharField(max_length=1, blank=True, null=True, verbose_name='性别')
    record_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='记录编号')

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = '健康数据'
        verbose_name_plural = '健康数据'