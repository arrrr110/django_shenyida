from django.db import models
from django.contrib.auth.models import User
from management.models import DeviceRecords

class UserTransactionInfo(models.Model):
    """
    用户建档事务表（主表）
    用户产生了“短信认证手机号”的行为记录表
    """
    # id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=50, verbose_name='用户小程序id')
    send_phone = models.CharField(max_length=50, verbose_name='用户对此手机号发起验证')
    coop_org_user_records_id = models.ForeignKey(User, models.SET_NULL, null=True, blank=True, verbose_name='归属机构')
    device_id = models.ForeignKey(DeviceRecords, models.SET_NULL, null=True, blank=True, verbose_name='归属设备')
    regist_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    class Meta:
        verbose_name = '用户建档事务表（主表）'
        verbose_name_plural = '用户建档事务表（主表）'

    def __str__(self):
        return f"用户建档事务记录 {self.id}"


class UserBaseInfoRecords(models.Model):
    """
    用户基础信息表(子表)
    验证通过后添加
    """
    # id = models.AutoField(primary_key=True)
    USER_TYPE_CHOICES = (
        (0, '设备和机构建立'),
        (1, '亲友建立')
    )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0, verbose_name='建档方式')
    transaction_info_id = models.ForeignKey(UserTransactionInfo, 
                                            models.CASCADE, 
                                            verbose_name='用户建档事务记录外键')
    user_phone = models.CharField(max_length=100, verbose_name='手机号')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='用户的姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='用户的出生日期')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='用户的居住地址')
    GENDER_CHOICES = (
        (0, '未知'),
        (1, '男性'),
        (2, '女性')
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True, verbose_name='性别')
    height = models.IntegerField(null=True, blank=True, verbose_name='身高(cm)')
    weight = models.IntegerField(null=True, blank=True, verbose_name='体重(kg)')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '用户基础信息表(子表)'
        verbose_name_plural = '用户基础信息表(子表)'

    def __str__(self):
        return f"用户基础信息记录 {self.id}"


class UserRelativeRelationshipsRecords(models.Model):
    """
    用户亲友关系表
    用户在亲友建档栏目下，为亲友建档后插入关系数据
    """
    # id = models.AutoField(primary_key=True)
    # 前一个表软删除，这里的CASCADE没意义了
    transaction_info_id = models.ForeignKey(UserTransactionInfo, on_delete=models.CASCADE,
                                            verbose_name='用户建档事务记录外键')
    user_base_info_id = models.ForeignKey(UserBaseInfoRecords, on_delete=models.CASCADE,
                                          related_name='main_user_relations', verbose_name='主用户id')
    relative_id = models.ForeignKey(UserBaseInfoRecords, on_delete=models.CASCADE,
                                    related_name='relative_relations', verbose_name='亲友id')
    nicky_name = models.CharField(max_length=100, verbose_name='用户对亲友昵称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='建立时间')

    class Meta:
        verbose_name = '用户亲友关系表'
        verbose_name_plural = '用户亲友关系表'

    def __str__(self):
        return f"用户亲友关系记录 {self.id}"