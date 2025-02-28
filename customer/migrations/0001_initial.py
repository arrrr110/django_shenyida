# Generated by Django 5.1.6 on 2025-02-27 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBaseInfoRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[(0, '设备和机构建立'), (1, '亲友建立')], default=0, verbose_name='建档方式')),
                ('user_phone', models.CharField(max_length=100, verbose_name='手机号')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户的姓名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='用户的出生日期')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='用户的居住地址')),
                ('gender', models.IntegerField(blank=True, choices=[(0, '未知'), (1, '男性'), (2, '女性')], null=True, verbose_name='性别')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='身高(cm)')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='体重(kg)')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '用户基础信息表(子表)',
                'verbose_name_plural': '用户基础信息表(子表)',
            },
        ),
        migrations.CreateModel(
            name='UserTransactionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50, verbose_name='用户小程序id')),
                ('send_phone', models.CharField(max_length=50, verbose_name='用户对此手机号发起验证')),
                ('regist_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('coop_org_user_records_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='归属机构')),
                ('device_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.devicerecords', verbose_name='归属设备')),
            ],
            options={
                'verbose_name': '用户建档事务表（主表）',
                'verbose_name_plural': '用户建档事务表（主表）',
            },
        ),
        migrations.CreateModel(
            name='UserRelativeRelationshipsRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nicky_name', models.CharField(max_length=100, verbose_name='用户对亲友昵称')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='建立时间')),
                ('relative_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relative_relations', to='customer.userbaseinforecords', verbose_name='亲友id')),
                ('user_base_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_user_relations', to='customer.userbaseinforecords', verbose_name='主用户id')),
                ('transaction_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.usertransactioninfo', verbose_name='用户建档事务记录外键')),
            ],
            options={
                'verbose_name': '用户亲友关系表',
                'verbose_name_plural': '用户亲友关系表',
            },
        ),
        migrations.AddField(
            model_name='userbaseinforecords',
            name='transaction_info_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.usertransactioninfo', verbose_name='用户建档事务记录外键'),
        ),
    ]
