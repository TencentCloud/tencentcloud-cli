**Example 1: 获取设备信息**

获取设备信息

Input: 

```
tccli iot GetDevice --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "e8d61efa-80a7-495a-a0cb-8d2d4698d354",
        "Device": {
            "DeviceSecret": "2e0e56544c1e1e548725c79346f409c9",
            "ProductId": "iot-4e0wsxpi",
            "DeviceName": "abc",
            "CreateTime": "2018-06-11 15:19:41",
            "DeviceInfo": "{\"product\":\"iot-4e0wsxpi\",\"device\":\"abc\",\"sdk-ver\":\"2.3\",\"firm-ver\":\"LINUX_V1.0\",\"topic\":\"ota\\/update\\/iot-4e0wsxpi\\/abc\"}",
            "UpdateTime": "2018-06-19 20:46:34"
        }
    }
}
```

