**Example 1: 机动车登记证书识别示例代码**

机动车登记证书识别示例代码

Input: 

```
tccli ocr VehicleRegCertOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/vehicle/VehicleRegCertOCR/VehicleRegCertOCR1.jpg
```

Output: 
```
{
    "Response": {
        "VehicleRegCertInfos": [
            {
                "Name": "编号",
                "Value": "*310005169880*"
            },
            {
                "Name": "机动车所有人1",
                "Value": "李明"
            },
            {
                "Name": "车辆识别代号/车架号",
                "Value": "LFV8"
            },
            {
                "Name": "身份证明名称1",
                "Value": "居民身份证"
            },
            {
                "Name": "号码1",
                "Value": "339001198706168418"
            }
        ],
        "RequestId": "393fa9e0-3827-4183-9fe7-68ed622028a1"
    }
}
```

