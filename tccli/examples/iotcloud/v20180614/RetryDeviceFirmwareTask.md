**Example 1: 查询固件升级任务详情**



Input: 

```
tccli iotcloud RetryDeviceFirmwareTask --cli-unfold-argument  \
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

