**Example 1: 创建设备（采用非对称加密）**



Input: 

```
tccli iotcloud CreateDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName test_device \
    --Attribute.Tags.0.Tag note \
    --Attribute.Tags.0.Type 2 \
    --Attribute.Tags.0.Value test_note
```

Output: 
```
{
    "Response": {
        "DeviceName": "test_device",
        "DevicePsk": "",
        "DeviceCert": "xxxxxxxxxxxxxxxxxxxx",
        "DevicePrivateKey": "xxxxxxxxxxxxxxxxxxxxxxx",
        "LoraDevEui": "",
        "LoraMoteType": "",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

**Example 2: 创建设备（采用对称加密）**



Input: 

```
tccli iotcloud CreateDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName test_device \
    --Attribute.Tags.0.Tag note \
    --Attribute.Tags.0.Type 2 \
    --Attribute.Tags.0.Value test_note
```

Output: 
```
{
    "Response": {
        "DeviceName": "test_device",
        "DevicePsk": "xxxxxxxxxxxxx",
        "DeviceCert": "",
        "DevicePrivateKey": "",
        "LoraDevEui": "",
        "LoraMoteType": "",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

