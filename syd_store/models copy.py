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

# 血氧模型
class BloodOxygen(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='所属设备')
    xy_n = models.CharField(max_length=20, verbose_name='血氧正常范围')
    address = models.CharField(max_length=200, blank=True, verbose_name='地址')
    user_id = models.CharField(max_length=20, verbose_name='用户ID')
    login_type = models.CharField(max_length=1, verbose_name='登录类型')
    measure_time = models.DateTimeField(verbose_name='测量时间')
    birthday = models.CharField(max_length=10, blank=True, verbose_name='生日')
    bpm = models.IntegerField(verbose_name='心率')
    xy_s = models.IntegerField(verbose_name='血氧状态码')
    xy = models.IntegerField(verbose_name='血氧值')
    age = models.IntegerField(verbose_name='年龄')
    bpm_n = models.CharField(max_length=20, verbose_name='心率正常范围')
    name = models.CharField(max_length=50, verbose_name='姓名')
    bpm_s = models.IntegerField(verbose_name='心率状态码')
    sex = models.CharField(max_length=1, verbose_name='性别')
    record_no = models.CharField(max_length=20, verbose_name='记录编号')

    def __str__(self):
        return self.record_no

    class Meta:
        verbose_name = '血氧数据'
        verbose_name_plural = '血氧数据'

# 血压模型
class BloodPressure(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='所属设备')
    address = models.CharField(max_length=200, blank=True, verbose_name='地址')
    user_id = models.CharField(max_length=20, verbose_name='用户ID')
    login_type = models.CharField(max_length=1, verbose_name='登录类型')
    hrR_s = models.IntegerField(verbose_name='心率状态码（血压）')
    sbpR_n = models.CharField(max_length=20, verbose_name='收缩压正常范围')
    measure_time = models.DateTimeField(verbose_name='测量时间')
    dbpR_s = models.IntegerField(verbose_name='舒张压状态码')
    dbpR = models.IntegerField(verbose_name='舒张压值')
    sbpR = models.IntegerField(verbose_name='收缩压值')
    hrR = models.IntegerField(verbose_name='心率值（血压）')
    birthday = models.CharField(max_length=10, blank=True, verbose_name='生日')
    age = models.IntegerField(verbose_name='年龄')
    sbpR_s = models.IntegerField(verbose_name='收缩压状态码')
    name = models.CharField(max_length=50, verbose_name='姓名')
    sex = models.CharField(max_length=1, verbose_name='性别')
    hrR_n = models.CharField(max_length=20, verbose_name='心率正常范围（血压）')
    record_no = models.CharField(max_length=20, verbose_name='记录编号')
    dbpR_n = models.CharField(max_length=20, verbose_name='舒张压正常范围')

    def __str__(self):
        return self.record_no

    class Meta:
        verbose_name = '血压数据'
        verbose_name_plural = '血压数据'

# 身高体重模型
class HeightWeight(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name='所属设备')
    address = models.CharField(max_length=200, verbose_name='地址')
    user_id = models.CharField(max_length=20, verbose_name='用户ID')
    login_type = models.CharField(max_length=1, verbose_name='登录类型')
    measure_time = models.DateTimeField(verbose_name='测量时间')
    bmi_s = models.IntegerField(verbose_name='BMI状态码')
    bmi = models.FloatField(verbose_name='BMI值')
    height = models.FloatField(verbose_name='身高')
    nation = models.CharField(max_length=20, verbose_name='民族')
    birthday = models.DateField(verbose_name='生日')
    weight = models.FloatField(verbose_name='体重')
    age = models.IntegerField(verbose_name='年龄')
    weight_n = models.CharField(max_length=20, verbose_name='体重正常范围')
    name = models.CharField(max_length=50, verbose_name='姓名')
    weight_s = models.IntegerField(verbose_name='体重状态码')
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期')
    sex = models.CharField(max_length=1, verbose_name='性别')
    department = models.CharField(max_length=100, verbose_name='部门')
    record_no = models.CharField(max_length=20, verbose_name='记录编号')
    bmi_n = models.CharField(max_length=20, verbose_name='BMI正常范围')

    def __str__(self):
        return self.record_no

    class Meta:
        verbose_name = '身高体重数据'
        verbose_name_plural = '身高体重数据'