**Example 1: 批量更新固件**



Input: 

```
tccli iotvideo BatchUpdateFirmware --cli-unfold-argument  \
    --ProductID product \
    --FirmwareVersion 2.0.0 \
    --FirmwareOriVersion 1.0.0
```

Output: 
```
{
    "Response": {
        "TaskId": 1,
        "RequestId": "id"
    }
}
```

