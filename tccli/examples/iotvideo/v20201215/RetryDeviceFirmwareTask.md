**Example 1: 重试设备升级任务**



Input: 

```
tccli iotvideo RetryDeviceFirmwareTask --cli-unfold-argument  \
    --ProductID product \
    --FirmwareVersion 1.0.0 \
    --TaskId 10000 \
    --DeviceName dev
```

Output: 
```
{
    "Response": {
        "RequestId": "id"
    }
}
```

