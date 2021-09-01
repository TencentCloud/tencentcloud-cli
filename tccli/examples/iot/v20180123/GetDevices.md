**Example 1: 获取设备列表**

获取设备列表

Input: 

```
tccli iot GetDevices --cli-unfold-argument  \
    --ProductId iot-5aawn3i8 \
    --Offset 0 \
    --Length 2
```

Output: 
```
{
    "Response": {
        "RequestId": "296bd834-169f-4056-a3a6-17a4992c7548",
        "Devices": [
            {
                "DeviceSecret": "632fe1778a19fcd997d936305851c0bc",
                "ProductId": "iot-5aawn3i8",
                "DeviceName": "device2",
                "CreateTime": "2018-06-22 14:59:43"
            },
            {
                "DeviceSecret": "19e5ccc3f9918875c11839b35e7e5215",
                "ProductId": "iot-5aawn3i8",
                "DeviceName": "device1",
                "CreateTime": "2018-06-22 14:59:38"
            }
        ],
        "Total": 2
    }
}
```

