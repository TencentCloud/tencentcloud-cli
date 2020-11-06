**Example 1: 获取lora设备详情**



Input: 

```
tccli iotcloud DescribeLoraDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName test_device
```

Output: 
```
{
    "Response": {
        "AppEui": "0000000000000001",
        "DeviceEui": "ffffff100000a680",
        "ClassType": "A",
        "AppKey": "98929b92f09e2daf676d646d0f61d258",
        "ProductId": "ABCDE12345",
        "DeviceName": "test_device",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

