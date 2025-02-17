from django.db import models

# 设备模型
class Device(models.Model):
    device_model = models.CharField(max_length=10, verbose_name='设备型号')
    unit_name = models.CharField(max_length=100, blank=True, verbose_name='单位名称')
    unit_no = models.CharField(max_length=20, verbose_name='单位编号')
    mac_addr = models.CharField(max_length=20, verbose_name='设备MAC地址')
    device_no = models.CharField(max_length=20, verbose_name='设备编号')

    def __str__(self):
        return self.device_no

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'

# 合并后的健康数据模型
class HealthData(models.Model):
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
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='所属设备')
     # 数据类型
    data_type = models.CharField(max_length=50, choices=DATA_TYPE_CHOICES, blank=True, null=True, verbose_name='数据类型')

    # 心率相关
    bpm_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='心率正常范围')
    bpm_s = models.IntegerField(blank=True, null=True, verbose_name='心率状态码')
    bpm = models.IntegerField(blank=True, null=True, verbose_name='心率')
    # 血氧相关字段
    xy_n = models.CharField(max_length=20, blank=True, null=True, verbose_name='血氧正常范围')
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
    address = models.CharField(max_length=200, blank=True, verbose_name='地址')
    user_id = models.CharField(max_length=20, verbose_name='用户ID')
    login_type = models.CharField(max_length=1, verbose_name='登录类型')
    measure_time = models.DateTimeField(verbose_name='测量时间')
    birthday = models.CharField(max_length=10, blank=True, verbose_name='生日')
    age = models.IntegerField(verbose_name='年龄')
    name = models.CharField(max_length=50, verbose_name='姓名')
    sex = models.CharField(max_length=1, verbose_name='性别')
    record_no = models.CharField(max_length=20, verbose_name='记录编号')

    def __str__(self):
        return self.record_no

    class Meta:
        verbose_name = '健康数据'
        verbose_name_plural = '健康数据'