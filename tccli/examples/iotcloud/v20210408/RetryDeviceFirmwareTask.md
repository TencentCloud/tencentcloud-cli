**Example 1: 查询固件升级任务详情**



Input: 

```
tccli iotcloud RetryDeviceFirmwareTask --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --FirmwareVersion 1.0.0 \
    --TaskId 10000 \
    --DeviceName dev
```

Output: 
```
{
    "Response": {
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbc"
    }
}
```

