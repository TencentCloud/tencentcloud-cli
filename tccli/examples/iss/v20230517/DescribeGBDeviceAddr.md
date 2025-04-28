**Example 1: 错误**

包含无效的DeviceId

Input: 

```
tccli iss DescribeGBDeviceAddr --cli-unfold-argument  \
    --DeviceIds null
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.ContainInvalidDeviceId",
            "Message": "包含无效的DeviceId"
        },
        "RequestId": "1cb1df16-8c29-****-****-e3283cea4958"
    }
}
```

**Example 2: 成功**

success

Input: 

```
tccli iss DescribeGBDeviceAddr --cli-unfold-argument  \
    --DeviceIds 3db****e3-****-****-b7be-****4be705d
```

Output: 
```
{
    "Response": {
        "Data": {
            "RemoteAddrs": [
                {
                    "Addr": "127.0.0.1",
                    "DeviceId": "3db****e3-****-****-b7be-****4be705d"
                }
            ]
        },
        "RequestId": "887e50f0-****-****-a37d-c88b****19e3"
    }
}
```

