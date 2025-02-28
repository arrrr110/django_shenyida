import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # 替换为你的项目的settings模块

import django
django.setup()

from management.models import TestTypeMapping, DeviceRecords, ArticleRecords
from logger.models import LogAuditInfo
from organization.models import OrgCustomTestSchemeMapping
from syd_store.models import TestTransactionInfo, UserCheckupSingleRecords, Device, HealthData
from django.contrib.auth.models import User


def inject_test_data():
    # 创建用户
    user = User.objects.create_user(username='testuser', password='testpassword')

    # 注入10条TestTypeMapping数据
    for i in range(10):
        test_type_mapping = TestTypeMapping.objects.create(
            detection_name=f'测试检测项目{i}',
            normal_range='10-20',
            unit_of_measurement='mg',
            feature_field='特征字段',
            creator_instructions='这是一个测试项目'
        )

    # 注入10条DeviceRecords数据
    for i in range(10):
        device_records = DeviceRecords.objects.create(
            coop_org_user_records_id=user,
            device_deployment_address=f'测试地址{i}',
            device_type='测试类型',
            device_number=f'D00{i + 1}',
            device_remark='测试备注'
        )

    # 注入10条ArticleRecords数据
    for i in range(10):
        article_records = ArticleRecords.objects.create(
            article_title=f'测试文章标题{i}',
            article_content=f'这是一篇测试文章{i}',
            detection_project_type_id=TestTypeMapping.objects.first()
        )

    # 注入10条LogAuditInfo数据
    for i in range(10):
        log_audit_info = LogAuditInfo.objects.create(
            table_name='TestTypeMapping',
            data_id=TestTypeMapping.objects.first().id,
            operator_id=user.id,
            before_data={'detection_name': f'旧名称{i}'},
            after_data={'detection_name': f'新名称{i}'}
        )

    # 注入10条OrgCustomTestSchemeMapping数据
    for i in range(10):
        org_custom_test_scheme_mapping = OrgCustomTestSchemeMapping.objects.create(
            coop_org_user_records_id=user,
            package_name=f'测试套餐{i}',
            detection_projects='项目1_项目2',
            description='这是一个测试套餐'
        )

    # 注入10条TestTransactionInfo数据
    for i in range(10):
        test_transaction_info = TestTransactionInfo.objects.create(
            user_id=f'123456{i}',
            test_type_id=TestTypeMapping.objects.first(),
            coop_org_user_records_id=user,
            device_records_id=DeviceRecords.objects.first()
        )

    # 注入10条UserCheckupSingleRecords数据
    for i in range(10):
        user_checkup_single_records = UserCheckupSingleRecords.objects.create(
            text_key=f'xy{i}',
            text_value=f'96{i}',
            unit_of_measurement='mg',
            test_info_id=TestTransactionInfo.objects.first()
        )

    # 注入10条Device数据
    for i in range(10):
        device = Device.objects.create(
            device_model=f'D0{i + 1}',
            unit_name='测试单位',
            unit_no=f'U00{i + 1}',
            mac_addr=f'00:11:22:33:44:{55 + i}',
            device_no=f'D00{i + 2}'
        )

    # 注入10条HealthData数据
    for i in range(10):
        health_data = HealthData.objects.create(
            device=Device.objects.first(),
            data_type='血压心率',
            bpm_n='60-100',
            bpm_s=1,
            bpm=70,
            user_id=f'U00{i + 1}'
        )


if __name__ == '__main__':
    inject_test_data()
    print('测试数据注入完成')