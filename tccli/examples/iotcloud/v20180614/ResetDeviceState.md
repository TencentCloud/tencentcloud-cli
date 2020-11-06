**Example 1: 重置设备连接状态**



Input: 

```
tccli iotcloud ResetDeviceState --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceNames test_device1 test_device2
```

Output: 
```
{
    "Response": {
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c",
        "SuccessCount": 1,
        "ResetDeviceResults": [
            {
                "DeviceName": "test_device1",
                "Success": true,
                "Reason": ""
            },
            {
                "DeviceName": "test_device2",
                "Success": false,
                "Reason": "device not exists"
            }
        ]
    }
}
```

