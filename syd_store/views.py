# views.py
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt # django-rest-farmework不考虑csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device, HealthData
from .serializers import DeviceSerializer, HealthDataSerializer
import json
from datetime import datetime
# from django.utils import timezone
import pytz
import logging

# 配置日志
logger = logging.getLogger(__name__)
# 设置中国时区
china_tz = pytz.timezone('Asia/Shanghai')

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

class IndexView(APIView):
    """
    接收 POST 请求并将数据分类注入到特定表中的视图类
    """
    def post(self, request, *args, **kwargs):
        try:
            # 使用 request.data 来获取JSON数据
            data = request.data
            logger.info(f"Received POST data: {data}")  # 记录接收到的POST数据
            device_model = data.get('deviceModel')
            unit_name = data.get('unitName')
            unit_no = data.get('unitNo')
            mac_addr = data.get('macAddr')
            device_no = data.get('deviceNo')

            # 获取或创建设备实例
            device, created = Device.objects.get_or_create(
                device_model=device_model,
                unit_name=unit_name,
                unit_no=unit_no,
                mac_addr=mac_addr,
                device_no=device_no
            )
            if created:
                logger.info(f"Created new device: {device}")  # 记录新设备的创建
            else:
                logger.info(f"Using existing device: {device}")  # 记录使用已存在的设备

            # 确定数据类型
            data_type = None
            if device_model == 'X10':
                if 'xy_n' in data['datas'][0]:
                    data_type = '血氧测量'
                elif 'hrR_s' in data['datas'][0]:
                    data_type = '血压心率'
            elif device_model == 'X15_6':
                data_type = '身高体重'

            if data_type not in [choice[0] for choice in DATA_TYPE_CHOICES]:
                data_type = None
                logger.info("Data type not recognized, setting to None")  # 记录数据类型未识别

            # 处理数据
            health_data = data['datas'][0]
            measure_time = datetime.strptime(health_data.get('measureTime'), '%Y-%m-%d %H:%M:%S')
            # 转换为中国时区
            measure_time = china_tz.localize(measure_time)

            # 处理日期字段
            birthday = health_data.get('birthday')
            start_date = health_data.get('startDate')
            end_date = health_data.get('endDate')
            if birthday:
                birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
            if start_date:
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            if end_date:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            # 创建健康数据实例
            health_data_obj = HealthData.objects.create(
                device=device,
                data_type=data_type,
                # 心率相关
                bpm_n=health_data.get('bpm_n'),
                bpm_s=int(health_data.get('bpm_s')) if health_data.get('bpm_s') else None,
                bpm=int(health_data.get('bpm')) if health_data.get('bpm') else None,
                # 血氧相关字段
                xy_n=health_data.get('xy_n'),
                xy_s=int(health_data.get('xy_s')) if health_data.get('xy_s') else None,
                xy=int(health_data.get('xy')) if health_data.get('xy') else None,
                # 血压相关字段
                hrR_s=int(health_data.get('hrR_s')) if health_data.get('hrR_s') else None,
                sbpR_n=health_data.get('sbpR_n'),
                dbpR_s=int(health_data.get('dbpR_s')) if health_data.get('dbpR_s') else None,
                dbpR=int(health_data.get('dbpR')) if health_data.get('dbpR') else None,
                sbpR=int(health_data.get('sbpR')) if health_data.get('sbpR') else None,
                hrR=int(health_data.get('hrR')) if health_data.get('hrR') else None,
                sbpR_s=int(health_data.get('sbpR_s')) if health_data.get('sbpR_s') else None,
                hrR_n=health_data.get('hrR_n'),
                dbpR_n=health_data.get('dbpR_n'),
                # 身高体重相关字段
                bmi_s=int(health_data.get('bmi_s')) if health_data.get('bmi_s') else None,
                bmi=float(health_data.get('bmi')) if health_data.get('bmi') else None,
                height=float(health_data.get('height')) if health_data.get('height') else None,
                nation=health_data.get('nation'),
                weight=float(health_data.get('weight')) if health_data.get('weight') else None,
                weight_n=health_data.get('weight_n'),
                weight_s=int(health_data.get('weight_s')) if health_data.get('weight_s') else None,
                start_date=start_date,
                end_date=end_date,
                department=health_data.get('department'),
                bmi_n=health_data.get('bmi_n'),
                # 公共字段
                address=health_data.get('address'),
                user_id=health_data.get('userID'),
                login_type=health_data.get('loginType'),
                measure_time=measure_time,
                birthday=birthday,
                age=int(health_data.get('age')) if health_data.get('age') else None,
                name=health_data.get('name'),
                sex=health_data.get('sex'),
                record_no=health_data.get('recordNo')
            )
            logger.info(f"Created health data object: {health_data_obj}")  # 记录健康数据对象的创建

            serializer = HealthDataSerializer(health_data_obj)
            logger.info(f"Serialized data: {serializer.data}")  # 记录序列化后的数据
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"An error occurred: {str(e)}", exc_info=True)  # 记录错误信息和堆栈跟踪
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        logger.info("Received GET request, but it's not allowed")  # 记录接收到不允许的GET请求
        return Response({'status': 'error', 'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)