**Example 1: 服务下发消息到lora设备**



Input: 

```
tccli iotcloud PublishToDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName test_device \
    --Port 8000 \
    --Payload hello
```

Output: 
```
{
    "Response": {
        "RequestId": "54f75f05-a87c-45fc-9520-6b59e251e91c"
    }
}
```

