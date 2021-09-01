**Example 1: 获取创建多设备结果**



Input: 

```
tccli iotcloud DescribeMultiDevices --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --TaskId abcdefghijklmn \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TaskId": "abcdedf123456789",
        "TotalDevNum": 2,
        "DevicesInfo": [
            {
                "DeviceName": "test_device1",
                "DeviceCert": "-----BEGIN CERTIFICATE-----\n-----END CERTIFICATE-----",
                "DevicePrivateKey": "-----BEGIN PRIVATE KEY-----\n-----END PRIVATE KEY-----\n",
                "Result": 0
            },
            {
                "DeviceName": "test_device2",
                "Result": 2001
            }
        ],
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

