**Example 1: 获取设备数据**

获取设备数据

Input: 

```
tccli iot GetDeviceData --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceName device1
```

Output: 
```
{
    "Response": {
        "RequestId": "a7c30659-fd9c-4f34-b10d-c3d3c9b49c09",
        "DeviceData": "{\"light\":{\"value\":\"on\",\"timestamp\":1520868197}}"
    }
}
```

