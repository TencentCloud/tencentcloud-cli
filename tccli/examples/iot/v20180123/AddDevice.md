**Example 1: 新增设备**

新增设备

Input: 

```
tccli iot AddDevice --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceName aaaa
```

Output: 
```
{
    "Response": {
        "RequestId": "98abdf39-fb5d-4314-8b62-ec749951f75f",
        "Device": {
            "DeviceSecret": "f1c8058428adab76b0b61cafb435ec62",
            "ProductId": "iot-4e0wsxpi",
            "DeviceName": "aaaa",
            "CreateTime": "2018-07-06 01:46:43",
            "DeviceInfo": "{}",
            "UpdateTime": "2018-07-06 01:46:43"
        }
    }
}
```

