**Example 1: 创建lora类型的设备**



Input: 

```
tccli iotcloud CreateLoraDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName test_device \
    --AppEui 0000000000000001 \
    --DeviceEui ffffff100000a680 \
    --AppKey 98929b92f09e2daf676d646d0f61d258 \
    --DeviceType A \
    --AuthKey 009edbf44ec1a36cd72663973761e615 \
    --Memo memotext
```

Output: 
```
{
    "Response": {
        "AppEui": "0000000000000001",
        "DeviceEui": "ffffff100000a680",
        "ClassType": "A",
        "DeviceName": "test_device",
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

