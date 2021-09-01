**Example 1: 获取绑定设备数据**

获取绑定设备数据

Input: 

```
tccli iot AppGetDeviceData --cli-unfold-argument  \
    --AccessToken xxx \
    --ProductId iot-a8ojgbji \
    --DeviceName device
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

