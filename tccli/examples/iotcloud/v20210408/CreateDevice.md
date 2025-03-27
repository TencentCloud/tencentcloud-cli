**Example 1: 创建设备（采用对称加密）**



Input: 

```
tccli iotcloud CreateDevice --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --DeviceName dev-001 \
    --Attribute.Tags.0.Tag note \
    --Attribute.Tags.0.Type 2 \
    --Attribute.Tags.0.Value test_note
```

Output: 
```
{
    "Response": {
        "DeviceName": "dev-001",
        "DevicePsk": "9MTpKyUBRpsPLB3hQyVfeQ==",
        "DeviceCert": "",
        "DevicePrivateKey": "9MTpKyUBRpsP",
        "LoraDevEui": "1",
        "LoraMoteType": 1,
        "LoraNwkKey": "ddgergsdfretger",
        "LoraAppKey": "3fgrtsdfsdgfdga",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

**Example 2: 创建设备（采用非对称加密）**



Input: 

```
tccli iotcloud CreateDevice --cli-unfold-argument  \
    --ProductId UTY5QRLMQY \
    --DeviceName dev-001
```

Output: 
```
{
    "Response": {
        "DeviceName": "dev-001",
        "DevicePsk": "9MTpKyUBRpsPLB3hQyVfeQ==",
        "DeviceCert": "-----BEGIN CERTIFICATE----- MIIFGjCCBAKgAwIBAgIQCgRw0Ja8ihLIkKbf",
        "DevicePrivateKey": "-----BEGIN PRIVATE KEY----- MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgw",
        "LoraDevEui": "1",
        "LoraMoteType": 1,
        "LoraNwkKey": "ddgergsdfretger",
        "LoraAppKey": "3fgrtsdfsdgfdga",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

