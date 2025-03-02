import requests
import json


url = 'http://127.0.0.1:8000/test/'  # 替换为你的实际域名

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    for index, item in enumerate(data):
        json_item = json.dumps(item, ensure_ascii=False, indent=4)
        # 将 JSON 字符串转换为 Python 对象
        python_obj = json.loads(json_item)  
        print(f"get: {index} - {python_obj['data_type']} - {python_obj['record_no']}")
else:
    print(f"Error: {response.status_code} - {response.text}")