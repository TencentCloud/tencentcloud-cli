**Example 1: 重置设备**

重置设备

Input: 

```
tccli iot ResetDevice --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceName device1
```

Output: 
```
{
    "Response": {
        "RequestId": "1638c57e-1573-4aa7-b459-aada7143ee5c",
        "Device": {
            "ProductId": "iot-4e0wsxpi",
            "DeviceName": "device1",
            "DeviceSecret": "bb171a7a3a8aa1b935f1172043fbd0f6",
            "UpdateTime": "2018-03-29 20:36:45",
            "CreateTime": "2018-03-22 12:41:04",
            "DeviceInfo": {}
        }
    }
}
```

