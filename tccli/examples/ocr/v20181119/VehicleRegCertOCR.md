**Example 1: 机动车登记证书识别示例代码**

机动车登记证书识别示例代码

Input: 

```
tccli ocr VehicleRegCertOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "VehicleRegCertInfos": [
            {
                "Name": "车辆型号",
                "Value": "FV7"
            },
            {
                "Name": "发动机号",
                "Value": "S26"
            },
            {
                "Name": "车辆识别代号/车架号",
                "Value": "LFV8"
            },
            {
                "Name": "制造厂名称",
                "Value": "一汽大众汽车有限公司"
            },
            {
                "Name": "机动车所有人/身份证明名称/号码",
                "Value": "小明/居民身份证/584874705102015"
            }
        ],
        "RequestId": "393fa9e0-3827-4183-9fe7-68ed622028a1"
    }
}
```

