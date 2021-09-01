**Example 1: 获取设备统计指标**

获取设备统计指标

Input: 

```
tccli iot GetDeviceStatistics --cli-unfold-argument  \
    --StartDate 2018-04-19 \
    --EndDate 2018-04-23
```

Output: 
```
{
    "Response": {
        "RequestId": "d1d98b19-a1b4-41df-95fd-c02797f802c4",
        "DeviceStatistics": [
            {
                "Datetime": "2018-04-20 00:00:00",
                "DeviceOnline": 0,
                "DeviceActive": 0,
                "DeviceTotal": 11
            },
            {
                "Datetime": "2018-04-21 00:00:00",
                "DeviceOnline": 0,
                "DeviceActive": 0,
                "DeviceTotal": 0
            },
            {
                "Datetime": "2018-04-22 00:00:00",
                "DeviceOnline": 0,
                "DeviceActive": 0,
                "DeviceTotal": 0
            },
            {
                "Datetime": "2018-04-23 00:00:00",
                "DeviceOnline": 0,
                "DeviceActive": 0,
                "DeviceTotal": 0
            }
        ]
    }
}
```

