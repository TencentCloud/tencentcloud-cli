**Example 1: 模拟lora类型的设备向服务器发送消息**



Input: 

```
tccli iotcloud PublishAsDevice --cli-unfold-argument  \
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

