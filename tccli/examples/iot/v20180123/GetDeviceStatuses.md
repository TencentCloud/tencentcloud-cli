**Example 1: 批量获取设备状态**



Input: 

```
tccli iot GetDeviceStatuses --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceNames device1 device2
```

Output: 
```
{
    "Response": {
        "RequestId": "3fa7d395-c1ff-4ede-beec-59afdeded8e9",
        "DeviceStatuses": [
            {
                "DeviceName": "device1",
                "Status": "inactive"
            },
            {
                "DeviceName": "device2",
                "Status": "inactive"
            }
        ]
    }
}
```

