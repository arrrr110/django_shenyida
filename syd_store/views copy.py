from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Device, BloodOxygen, BloodPressure, HeightWeight
import json
from datetime import datetime
from django.utils import timezone
import pytz

# 设置中国时区
china_tz = pytz.timezone('Asia/Shanghai')

@csrf_exempt
def index(request):
    """
    接收POST请求并将数据分类注入到特定表中的视图函数
    """
    if request.method == 'POST':
        try:
            # 解析JSON数据
            data = json.loads(request.body)
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

            # 根据设备模型分类处理数据
            if device_model == 'X10':
                print('识别为:血氧数据')
                # 处理血氧数据
                if 'xy_n' in data['datas'][0]:
                    blood_oxygen_data = data['datas'][0]
                    measure_time = datetime.strptime(blood_oxygen_data.get('measureTime'), '%Y-%m-%d %H:%M:%S')
                    # 转换为中国时区
                    measure_time = china_tz.localize(measure_time)
                    BloodOxygen.objects.create(
                        device=device,
                        xy_n=blood_oxygen_data.get('xy_n'),
                        address=blood_oxygen_data.get('address'),
                        user_id=blood_oxygen_data.get('userID'),
                        login_type=blood_oxygen_data.get('loginType'),
                        measure_time=measure_time,
                        birthday=blood_oxygen_data.get('birthday'),
                        bpm=int(blood_oxygen_data.get('bpm')),
                        xy_s=int(blood_oxygen_data.get('xy_s')),
                        xy=int(blood_oxygen_data.get('xy')),
                        age=int(blood_oxygen_data.get('age')),
                        bpm_n=blood_oxygen_data.get('bpm_n'),
                        name=blood_oxygen_data.get('name'),
                        bpm_s=int(blood_oxygen_data.get('bpm_s')),
                        sex=blood_oxygen_data.get('sex'),
                        record_no=blood_oxygen_data.get('recordNo')
                    )
                # 处理血压数据
                elif 'hrR_s' in data['datas'][0]:
                    print('识别为:血压数据')
                    blood_pressure_data = data['datas'][0]
                    measure_time = datetime.strptime(blood_pressure_data.get('measureTime'), '%Y-%m-%d %H:%M:%S')
                    # 转换为中国时区
                    measure_time = china_tz.localize(measure_time)
                    BloodPressure.objects.create(
                        device=device,
                        address=blood_pressure_data.get('address'),
                        user_id=blood_pressure_data.get('userID'),
                        login_type=blood_pressure_data.get('loginType'),
                        hrR_s=int(blood_pressure_data.get('hrR_s')),
                        sbpR_n=blood_pressure_data.get('sbpR_n'),
                        measure_time=measure_time,
                        dbpR_s=int(blood_pressure_data.get('dbpR_s')),
                        dbpR=int(blood_pressure_data.get('dbpR')),
                        sbpR=int(blood_pressure_data.get('sbpR')),
                        hrR=int(blood_pressure_data.get('hrR')),
                        birthday=blood_pressure_data.get('birthday'),
                        age=int(blood_pressure_data.get('age')),
                        sbpR_s=int(blood_pressure_data.get('sbpR_s')),
                        name=blood_pressure_data.get('name'),
                        sex=blood_pressure_data.get('sex'),
                        hrR_n=blood_pressure_data.get('hrR_n'),
                        record_no=blood_pressure_data.get('recordNo'),
                        dbpR_n=blood_pressure_data.get('dbpR_n')
                    )
            elif device_model == 'X15_6':
                # 处理身高体重数据
                print('识别为:身高数据')
                height_weight_data = data['datas'][0]
                measure_time = datetime.strptime(height_weight_data.get('measureTime'), '%Y-%m-%d %H:%M:%S')
                birthday = datetime.strptime(height_weight_data.get('birthday'), '%Y-%m-%d')
                start_date = datetime.strptime(height_weight_data.get('startDate'), '%Y-%m-%d')
                end_date = datetime.strptime(height_weight_data.get('endDate'), '%Y-%m-%d')
                # 转换为中国时区
                measure_time = china_tz.localize(measure_time)
                birthday = china_tz.localize(birthday)
                start_date = china_tz.localize(start_date)
                end_date = china_tz.localize(end_date)
                HeightWeight.objects.create(
                    device=device,
                    address=height_weight_data.get('address'),
                    user_id=height_weight_data.get('userID'),
                    login_type=height_weight_data.get('loginType'),
                    measure_time=measure_time,
                    bmi_s=int(height_weight_data.get('bmi_s')),
                    bmi=float(height_weight_data.get('bmi')),
                    height=float(height_weight_data.get('height')),
                    nation=height_weight_data.get('nation'),
                    birthday=birthday,
                    weight=float(height_weight_data.get('weight')),
                    age=int(height_weight_data.get('age')),
                    weight_n=height_weight_data.get('weight_n'),
                    name=height_weight_data.get('name'),
                    weight_s=int(height_weight_data.get('weight_s')),
                    start_date=start_date,
                    end_date=end_date,
                    sex=height_weight_data.get('sex'),
                    department=height_weight_data.get('department'),
                    record_no=height_weight_data.get('recordNo'),
                    bmi_n=height_weight_data.get('bmi_n')
                )

            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)