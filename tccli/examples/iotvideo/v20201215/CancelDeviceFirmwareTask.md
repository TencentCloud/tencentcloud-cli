**Example 1: 取消设备升级任务**



Input: 

```
tccli iotvideo CancelDeviceFirmwareTask --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --FirmwareVersion 1.0.0 \
    --TaskId 10000 \
    --DeviceName dev
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

