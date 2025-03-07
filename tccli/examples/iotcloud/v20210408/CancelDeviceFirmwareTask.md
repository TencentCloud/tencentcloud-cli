**Example 1: 查询固件升级任务详情**



Input: 

```
tccli iotcloud CancelDeviceFirmwareTask --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --FirmwareVersion 1.0.0 \
    --TaskId 10000 \
    --DeviceName dev01
```

Output: 
```
{
    "Response": {
        "RequestId": "0b77fcf9-d157-4b60-9a3d-541916b48c24"
    }
}
```

